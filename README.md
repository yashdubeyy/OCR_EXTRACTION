Patient Assessment Form OCR 🏥
Extract text from Patient Assessment Forms (JPG, JPEG, PDF) using OCR and store data in a database.


📌 Features
✔ Extracts text from JPEG, JPG, and PDF files
✔ Uses Tesseract OCR for text extraction
✔ Stores data in a PostgreSQL database
✔ Simple Streamlit web UI for uploading files
✔ Outputs extracted text in JSON format

🛠 Installation
1️⃣ Clone the Repository
git clone https://github.com/yashdubeyy/OCR_EXTRACTION.git
cd OCR_EXTRACTION


2️⃣ Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Install Tesseract OCR
Windows:
Download Tesseract OCR from here > https://github.com/UB-Mannheim/tesseract/wiki  and install it.
Then add Tesseract to your system PATH.

Mac/Linux:
sudo apt update && sudo apt install tesseract-ocr -y  # Ubuntu
brew install tesseract  # Mac

5️⃣ Install Poppler for PDF Support
Windows:
Download Poppler from this link and add it to PATH.  > https://github.com/oschwartz10612/poppler-windows/releases

Mac/Linux:
sudo apt install poppler-utils  # Ubuntu
brew install poppler  # Mac


🛢 Database Setup (PostgreSQL)
1️⃣ Install PostgreSQL
Download PostgreSQL and install it. > https://www.postgresql.org/download/

2️⃣ Create Database & User
CREATE DATABASE ocr_db;
CREATE USER ocr_user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ocr_db TO ocr_user;


3️⃣ Apply Database Schema
Run:
psql -U ocr_user -d ocr_db -f database_schema.sql


🚀 Usage
1️⃣ Run Streamlit App
streamlit run streamlit_app/app.py

🌐 Open http://localhost:8501 in your browser.

2️⃣ Upload a Patient Form
Drag and drop a JPG, JPEG, or PDF file.

3️⃣ View Extracted Data
Extracted text appears in JSON format
Data is automatically stored in PostgreSQL

🔍 Viewing Saved Data
Method 1: Using PostgreSQL CLI
psql -U ocr_user -d ocr_db

Then run:
SELECT * FROM patients;


Method 2: Using pgAdmin
Open pgAdmin
Navigate to ocr_db → patients
Run:
SELECT * FROM patients;


❌ Troubleshooting
1️⃣ Tesseract Not Found Error
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH.


Solution:

Ensure Tesseract is installed and added to PATH.
Try running:
tesseract -v

2️⃣ Poppler Not Installed Error
PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?


Solution:

Install Poppler:
brew install poppler # Mac
Add Poppler to PATH on Windows.


3️⃣ Database Authentication Failed
FATAL: password authentication failed for user "your_user"

Solution:

Check username/password in database_operations.py.
Reset password:
ALTER USER ocr_user WITH PASSWORD 'new_password';


📜 Folder Structure
OCR_EXTRACTION/
│── data/                      # Sample input files (JPG, PDF)
│── scripts/                   # Python scripts
│   ├── database_operations.py  # Handles database insertions
│   ├── ocr_extraction.py       # Extracts text from images & PDFs
│── streamlit_app/
│   ├── app.py                  # Streamlit web app
│── templates/
│   ├── sample_output.json       # Example extracted JSON
│── database_schema.sql          # SQL schema for PostgreSQL
│── requirements.txt             # Required Python packages
│── README.md                    # Documentation (this file)


🤝 Contributing
Fork the repository
Create a new branch (git checkout -b feature-name)
Commit changes (git commit -m "Added new feature")
Push (git push origin feature-name)
Open a Pull Request

