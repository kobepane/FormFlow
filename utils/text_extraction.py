import numpy as np
import ssl
import certifi


# # Set the SSL context to use certifi's certificate bundle
ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = ssl._create_unverified_context




from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from PIL import Image
import tempfile




def text_extract(img: Image.Image) -> list[str]:
   """
   Extract all words from a pre-processed PIL image and return them as a list of strings.
  
   Args:
       img (Image.Image): Pre-processed PIL image containing text.
  
   Returns:
       list[str]: A list of words extracted from the image.
   """
   # Save the PIL image to a temporary file
   with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
       img.save(temp_img.name)  # Save image in a format docTR can use
  
   # Load the image file with docTR
   img_doc = DocumentFile.from_images(temp_img.name)


   # Load a pre-trained OCR model
   model = ocr_predictor(pretrained=True)


   # Perform OCR on the document
   result = model(img_doc)


   # Extract words from the OCR result
   words = [word.value for block in result.pages[0].blocks for line in block.lines for word in line.words]
   return words






# This is what runs when the text extraction is needed
def run_text_extract(img: Image.Image) -> list[str]:
   if img:
       res: list[str] = text_extract(img)
   else:
       return FileNotFoundError()
   return res