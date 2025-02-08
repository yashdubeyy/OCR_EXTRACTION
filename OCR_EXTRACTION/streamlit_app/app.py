import sys
import os
# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.database_operations import insert_data_to_db
import streamlit as st
import json
from scripts.database_operations import insert_data_to_db
from scripts.ocr_extraction import extract_text_from_image, extract_text_from_pdf, extract_key_info


# Streamlit USER INTERFACE setup
st.title("Patient Assessment Form OCR")

# File uploader
uploaded_file = st.file_uploader("Upload a Patient Form (JPEG/PDF)", type=["jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    st.write("Processing the file...")

    # Check file type
    file_type = uploaded_file.type

    # Save uploaded file temporarily
    file_path = f"temp.{file_type.split('/')[-1]}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extract text based on file type
    if "pdf" in file_type:
        extracted_text = extract_text_from_pdf(file_path)
    else:
        extracted_text = extract_text_from_image(file_path)

    # Convert extracted text to structured JSON
    extracted_data = extract_key_info(extracted_text)

    # Display extracted JSON output
    st.subheader("Extracted Data (JSON)")
    st.json(extracted_data)

    # Store data in SQL database
    insert_data_to_db(extracted_data)
    st.success("Data successfully stored in the database.")
