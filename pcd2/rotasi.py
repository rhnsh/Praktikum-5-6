import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotate_image(image, degree):
    # Convert degrees to radians
    radian = np.radians(degree)
    cos_val, sin_val = np.cos(radian), np.sin(radian)

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate new image dimensions to fit rotated image
    max_dim = int(np.sqrt(height**2 + width**2))
    output_image = np.zeros((max_dim, max_dim, image.shape[2]), dtype=image.dtype)

    # Calculate center of the new output image
    center_y, center_x = max_dim // 2, max_dim // 2

    # Rotate each pixel from the original image
    for y in range(-height // 2, height // 2):
        for x in range(-width // 2, width // 2):
            new_x = int(cos_val * x - sin_val * y + center_x)
            new_y = int(sin_val * x + cos_val * y + center_y)

            # Check if the new coordinates are within the bounds of the output image
            if 0 <= new_x < max_dim and 0 <= new_y < max_dim:
                output_image[new_y, new_x] = image[y + height // 2, x + width // 2]

    return output_image

# Load the image
image_path = "C:\\Users\\muham\\OneDrive\\Gambar\\534826.jpg"
image = img.imread(image_path)

# Rotate the image by 45 degrees
rotated_image = rotate_image(image, 45)

# Display the original and rotated images
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated Image")

plt.show()
