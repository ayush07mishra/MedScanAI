import streamlit as st
import cv2
import pandas as pd
from fuzzywuzzy import process
import easyocr
from PIL import Image
import io
import pyheif

# Fixed path to the dataset (Update this path with your actual dataset path)
FIXED_DATASET_PATH = "Molecule_Dataset2.csv"  # Replace with the actual path to your CSV file

# Step 1: Convert HEIC to a Supported Format (e.g., JPG)
def convert_heic_to_supported_format(image_path, output_path="converted_image.jpg"):
    try:
        heif_file = pyheif.read(image_path)  # Read HEIC image
        image = Image.frombytes(
            heif_file.mode, heif_file.size, heif_file.data, heif_file.stride
        )  # Convert to PIL image
        image.save(output_path, format="JPEG")  # Save as JPG
        return output_path
    except Exception as e:
        raise ValueError(f"Failed to convert HEIC image: {str(e)}")

# Step 2: Preprocess the image using OpenCV
def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found or unable to read: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded

# Step 3: Extract text using EasyOCR
def recognize_text(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=False)  # Set gpu=True if you have a compatible GPU
    results = reader.readtext(image_path)

    # Extract detected text
    extracted_text = " ".join([result[1] for result in results])

    if not extracted_text:
        raise ValueError("No text detected in the image. Please check the image quality.")

    return extracted_text

# Step 4: Search for the molecule in the dataset
def lookup_molecule(extracted_text, dataset_path):
    # Load the dataset
    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

    # Clean column names (remove leading/trailing spaces)
    df.columns = df.columns.str.strip()

    # Verify if the 'Molecule Name' column exists
    if 'Molecule Name' not in df.columns:
        raise KeyError("The 'Molecule Name' column is missing in the dataset.")

    # Perform fuzzy matching to find the closest match
    best_match = process.extractOne(extracted_text, df['Molecule Name'])

    if best_match:
        # Get the best-matched row
        matched_row = df[df['Molecule Name'] == best_match[0]].to_dict('records')[0]
        return {"match": best_match[0], "score": best_match[1], "details": matched_row}
    else:
        return {"error": "Molecule not found in the dataset"}

# Step 5: Integrate everything into one function
def process_medicine_image(image_file, dataset_path=FIXED_DATASET_PATH):
    try:
        # Read the image from file
        image_path = "uploaded_image.jpg"
        with open(image_path, "wb") as f:
            f.write(image_file.getbuffer())

        # If the image is in HEIC format, convert it
        if image_path.lower().endswith(".heic"):
            st.write("Converting HEIC image to supported format...")
            image_path = convert_heic_to_supported_format(image_path)

        # Recognize text from the image
        extracted_text = recognize_text(image_path)

        # Lookup molecule in the dataset
        molecule_info = lookup_molecule(extracted_text, dataset_path)

        return molecule_info
    except Exception as e:
        return {"error": str(e)}

# Streamlit UI
st.title("Medicine Molecule Recognition")

st.write("Upload an image of a medicine to identify the molecule. The dataset is fixed and doesn't require uploading each time.")

# Upload image
uploaded_image = st.file_uploader("Choose an image (HEIC/JPG/PNG)", type=["heic", "jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Process the uploaded image and use the fixed dataset path
    result = process_medicine_image(uploaded_image)

    # Display the result
    if "error" in result:
        st.error(result["error"])
    else:
        st.write(f"Best Match: {result['match']}")
        st.write(f"Match Score: {result['score']}")
        st.write("Details:")
        st.json(result['details'])
else:
    st.warning("Please upload an image.")
