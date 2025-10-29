#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Manisha
#
# Created:     18-10-2025
# Copyright:   (c) Manisha 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json
import re
import csv
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import io

# Regex to remove non-digit characters
PHONE_RE_NON_DIGITS = re.compile(r'\D+')
VALID_START = ('6', '7', '8', '9')


def clean_number(raw):
    if raw is None:
        return ''
    return PHONE_RE_NON_DIGITS.sub('', str(raw))


def is_valid_indian_mobile(num):
    return len(num) == 10 and num[0] in VALID_START


def process_csv(file_data, column=None):
    text_stream = io.StringIO(file_data.decode('utf-8', errors='replace'))
    reader = csv.reader(text_stream)
    seen = set()
    total_valid = 0
    invalid = 0

    try:
        header = next(reader)
    except StopIteration:
        return {'total': 0, 'unique': 0, 'duplicate': 0, 'invalid': 0}

    # Determine which column to use
    if column is None:
        col_index = 0
    elif column.isdigit():
        col_index = int(column)
    else:
        lowered = [h.strip().lower() for h in header]
        if column.strip().lower() not in lowered:
            raise ValueError(f"Column '{column}' not found.")
        col_index = lowered.index(column.strip().lower())

    for row in reader:
        if not row:
            continue
        val = row[col_index] if col_index < len(row) else ''
        num = clean_number(val)
        if is_valid_indian_mobile(num):
            total_valid += 1
            seen.add(num)
        else:
            invalid += 1

    return {
        'total_count': total_valid,
        'unique_count': len(seen),
        'duplicate_count': total_valid - len(seen),
        'invalid_count': invalid
    }


class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/process':
            self.send_error(404, "Endpoint not found")
            return

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'},
        )
        if 'file' not in form:
            self.send_error(400, "Missing 'file' field in form data.")
            return

        uploaded_file = form['file']
        column = form['column'].value if 'column' in form else None

        filename = uploaded_file.filename or 'uploaded.csv'
        if not filename.lower().endswith('.csv'):
            self.send_error(400, "Only CSV files are supported.")
            return

        file_data = uploaded_file.file.read()

        try:
            result = process_csv(file_data, column)
        except ValueError as ve:
            self.send_error(400, str(ve))
            return
        except Exception as e:
            self.send_error(500, f"Processing error: {e}")
            return

        # Respond with JSON
        response = json.dumps(result).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        # Simple page for testing
        if self.path == '/':
            message = (
                "<html><body>"
                "<h2>Phone Number Processor</h2>"
                "<form method='POST' enctype='multipart/form-data' action='/process'>"
                "Select CSV file: <input type='file' name='file'><br><br>"
                "Column name or index (optional): <input type='text' name='column'><br><br>"
                "<input type='submit' value='Upload and Process'>"
                "</form></body></html>"
            )
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))
        else:
            self.send_error(404, "Page not found")


def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    print(f"Server running at http://localhost:{port}")
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
