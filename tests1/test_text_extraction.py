import sys
from pathlib import Path
# Add the FormFlow directory to the system path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from PIL import Image
from utils.text_extraction import text_extract  # Import your function

def test_extract_words_from_image():
    img_path = Path(__file__).parent / 'test-files' / 'Test.pil'  # Path to the image
    print(f"Looking for image at: {img_path}")

    try:
        img = Image.open(img_path)  # Load the image
        print("Image loaded successfully.")
    except FileNotFoundError:
        print("Image file not found. Please check the path.")
        return
    
    expected_words = ["This", "is", "a", "test", "document.", "HELLO", "WORLD."]  # Adjust based on your test image
    words = text_extract(img)

    print("Extracted words:", words)
    assert set(words) == set(expected_words)

if __name__ == '__main__':
    import pytest
    pytest.main()
