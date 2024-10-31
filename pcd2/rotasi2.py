import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotate_image_with_pivot(image, degree):
    # Convert degrees to radians
    radian = np.radians(degree)
    cos_val, sin_val = np.cos(radian), np.sin(radian)

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate new image dimensions to fit rotated image
    max_dim_x = int(abs(width * cos_val) + abs(height * sin_val))
    max_dim_y = int(abs(width * sin_val) + abs(height * cos_val))
    output_image = np.zeros((max_dim_y, max_dim_x, image.shape[2]), dtype=image.dtype)

    # Rotate each pixel from the original image around (0,0)
    for y in range(height):
        for x in range(width):
            new_x = int(cos_val * x - sin_val * y)
            new_y = int(sin_val * x + cos_val * y)

            # Shift new_x and new_y to positive coordinates in output image space
            if 0 <= new_x < max_dim_x and 0 <= new_y < max_dim_y:
                output_image[new_y, new_x] = image[y, x]

    return output_image

# Load the image
image_path = "C:\\Users\\muham\\OneDrive\\Gambar\\534826.jpg"
image = img.imread(image_path)

# Rotate the image by 45 degrees around (0, 0)
rotated_image = rotate_image_with_pivot(image, 45)

# Display the original and rotated images
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated Image (Pivot at Top-Left)")

plt.show()
