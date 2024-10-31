import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateAndResizeImage(image, degree, scale_factor):
    radian_deg = np.radians(degree)
    cos_deg = np.cos(radian_deg)
    sin_deg = np.sin(radian_deg)

    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2) * scale_factor)
    outputImage = np.zeros((max_dim, max_dim, image.dtype), dtype=np.uint8)

    centerY, centerX = max_dim//2, max_dim//2

    for y in range(-height//2, height//2):
        for x in range(-width//2, width//2):
            newX = int((x * cos_deg) + (y * sin_deg)) + centerX
            newY = int((-x * sin_deg) + (y * cos_deg)) + centerY
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[int(y*scale_factor+height//2), int(x*scale_factor+width//2)]

    return outputImage

image = img.imread("C:\\Users\\muham\\OneDrive\\Gambar\\Sent\\IMG-20211116-WA0007.jpg")
rotated_and_resized_image = rotateAndResizeImage(image, 45, 0.5)

plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(rotated_and_resized_image)

plt.subplots(1, 2, 1)
plt.imshow(image)

plt.subplots(1, 2, 2)
plt.imshow(rotated_and_resized_image)

plt.show()