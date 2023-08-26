import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def preprocess_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Resize the image to a fixed size
    image = cv2.resize(image, (200, 200))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray

def compare_images(image1, image2):
    # Calculate the structural similarity index
    similarity_index = ssim(image1, image2, data_range=image2.max() - image2.min())

    # Convert the similarity index to a percentage
    similarity_percentage = similarity_index * 100

    return similarity_percentage

# Example usage
image1_path = 'img2.jpg'
image2_path = 'output2.jfif'

# Preprocess the images
image1 = preprocess_image(image1_path)
image2 = preprocess_image(image2_path)

# Compare the images
similarity_percentage = compare_images(image1, image2)

print(f"The similarity percentage is: {similarity_percentage}%")
