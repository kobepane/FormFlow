from pdf2image import convert_from_bytes
import cv2
import numpy as np
from PIL import Image

# Convert PDF pages to images
def convert_pdf_to_images(pdf_bytes) -> Image.Image:
    images = convert_from_bytes(pdf_bytes)
    return images  # List of PIL Image objects

# Preprocess each image
def preprocess_image(pil_img) -> Image.Image:
    # Convert PIL image to OpenCV format
    # CHANGING!
    open_cv_image = np.array(pil_img[0].convert('RGB'))
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR for OpenCV

    # Convert to grayscale
    gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding (binarization)
    _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # Remove noise
    noise_removed_image = cv2.medianBlur(binary_image, 3)

    # Optionally resize or deskew the image here if needed

    # Convert back to PIL format for text extraction
    return Image.fromarray(noise_removed_image)

def run_preprocess(FILE):
    img: Image.Image = convert_pdf_to_images(FILE)
    pil_file = preprocess_image(img)
    return pil_file