from PIL import Image
import pytesseract


def text_extract(img: Image.Image) -> list[str]:
    """
    Extract all words from a pre-processed PIL image and return them as a list of strings.

    Args:
        img (Image.Image): Pre-processed PIL image containing text.

    Returns:
        list[str]: A list of words extracted from the image.
    """
    # Extract text from the image using pytesseract
    extracted_text = pytesseract.image_to_string(img)

    # Split the extracted text into individual words
    # This splits on spaces, newlines, and other whitespace characters
    words = extracted_text.split()
    return words

# this is what runs when the text extraction is needed
def run_text_extract(img: Image.Image) -> list[str]:
    if img:
        res: list[str] = text_extract(img)
    else:
        return FileNotFoundError()
    # return res
    return NotImplementedError()