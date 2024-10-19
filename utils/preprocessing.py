from utils.preprocessing import convert_pdf_to_images, preprocess_image
from PIL import Image
import matplotlib.pyplot as plt

# Load a sample PDF or image file for testing (replace 'sample.pdf' with your file path)
with open('/mnt/data/image.png', 'rb') as f:
    pdf_bytes = f.read()

# Convert PDF or image to list of images
pdf_images = convert_pdf_to_images(pdf_bytes)

# Preprocess each image
for i, img in enumerate(pdf_images):
    preprocessed_img = preprocess_image(img)

    # Step 3: Save or display preprocessed image for testing
    preprocessed_img.save(f'preprocessed_page_{i}.png')

    # Optionally, display the image using matplotlib
    plt.imshow(preprocessed_img)
    plt.title(f"Preprocessed Page {i + 1}")
    plt.show()
