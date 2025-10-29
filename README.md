# Phone Number Processing API (Python Standard Library)

A lightweight REST-style API built entirely using the *Python standard library* — no external dependencies required.  
This project processes an uploaded CSV file containing phone numbers, cleans and validates Indian mobile numbers, and returns JSON statistics with counts of valid, unique, duplicate, and invalid numbers.

---

## Features
- Runs on *pure Python* (no pip install needed)  
- Handles .csv file uploads via a simple web form or POST request  
- Cleans and normalizes phone numbers by removing non-digit characters  
- Validates *Indian mobile numbers*:
  - Must be *10 digits* long  
  - Must start with *6, 7, 8, or 9*  
- Returns JSON results with:
  - total_count: total valid mobile numbers  
  - unique_count: unique valid mobile numbers  
  - duplicate_count: repeated valid numbers  
  - invalid_count: invalid or malformed numbers  

---

## Project Structure

phone-number-processing-api-python/
│
├── main.py        # Main HTTP server script
├── README.md      # Documentation file
└── sample.csv     # Example input file (for testing)

## How It Works
1. Starts a simple HTTP server on *port 8000*
2. Provides a *web interface* at http://localhost:8000 to upload a CSV file
3. Processes the uploaded file:
   - Cleans each number (removes +91, spaces, brackets, hyphens, etc.)
   - Validates if it’s a 10-digit Indian mobile number
4. Returns a *JSON summary* with validation statistics

---

## Requirements
- Python *3.7 or higher*
- Works in any IDE including *PyScripter, **VS Code*, or the terminal
- No external libraries needed

---

## How to Run

### Option 1 — Run in PyScripter
1. Open main.py
2. Press *Run (F9)*  
3. Check the console output:

Server running at http://localhost:8000

### Option 2 — Run in Terminal
```bash
python main.py

Then open a browser and visit:
http://localhost:8000

---

## Performance
	•	Handles large CSV files efficiently (tested with 10L / 1 million numbers).
	•	Uses streaming to avoid high memory usage.
	•	Responds in under 15 seconds for large files on standard hardware.

---


## Example Use Case

This API can be used for:
	•	Cleaning large contact lists
	•	Verifying telecom or CRM data
	•	Filtering valid Indian mobile numbers
	•	Preparing marketing or SMS campaign data

---


## Author

Project: Phone Number Processing API (Python Standard Library)
Repository: phone-number-processing-api-python
Developed by: Manisha Mitra
Year: 2025


---


## License

This project is released under the MIT License — free to use, modify, and share.

### What to Do Next
1. Save this file as README.md in your repo.  
2. Replace your-username and Your Name with your actual GitHub username and name.  
3. Commit and push it — GitHub will render this beautifully with headings, tables, and code blocks.




