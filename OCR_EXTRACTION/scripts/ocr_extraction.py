import cv2
import pytesseract
from pdf2image import convert_from_path
import re
# Function to preprocess images for better OCR accuracy
def preprocess_image(image_path):
    """
    Preprocesses the image by converting it to grayscale and applying thresholding.
    This helps in improving OCR accuracy for both printed and handwritten text.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    """
    Uses OCR (Tesseract) to extract text from a processed image.
    """
    processed_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_img)
    return text

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):

    # Converts PDF pages into images and extracts text using OCR.

    images = convert_from_path(pdf_path)
    text = "\n".join([pytesseract.image_to_string(image) for image in images])
    return text

# Function to parse extracted text and convert it into structured JSON format
def extract_key_info(text):
    """
    Extracts important details such as patient name, DOB, assessment data,
    and medical inputs from the OCR text output.
    """
    data = {}

    # Extract basic patient details
    data['patient_name'] = re.search(r'Patient Name\s*:\s*(.*)', text).group(1).strip() if re.search(r'Patient Name\s*:\s*(.*)', text) else "Unknown"
    data['dob'] = re.search(r'DOB\s*:\s*(\d{2}/\d{2}/\d{4})', text).group(1).strip() if re.search(r'DOB\s*:\s*(\d{2}/\d{2}/\d{4})', text) else "Unknown"
    data['date'] = re.search(r'Date\s*:\s*(\d{2}/\d{2}/\d{4})', text).group(1).strip() if re.search(r'Date\s*:\s*(\d{2}/\d{2}/\d{4})', text) else "Unknown"
    
    # Extract Yes/No responses
    data['injection'] = "Yes" if "INJECTION : YES" in text else "No"
    data['exercise_therapy'] = "Yes" if "Exercise Therapy : YES" in text else "No"

    # Extract difficulty ratings
    ratings = {}
    for field in ["Bending", "Putting on Shoes", "Sleeping"]:
        match = re.search(fr"{field}:\s*(\d)", text)
        if match:
            ratings[field.lower().replace(" ", "_")] = int(match.group(1))
    data["difficulty_ratings"] = ratings

    return data