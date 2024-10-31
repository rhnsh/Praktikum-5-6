import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    # Create a copy of the image to avoid modifying the original
    imgTranslasi = np.copy(image)
    
    # Apply the translation using np.roll
    imgTranslasi = np.roll(imgTranslasi, shift=shiftY, axis=0)
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)

    # Set the appropriate regions to 0 after translation
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0
    if shiftX > 0: 
        imgTranslasi[:, :shiftX] = 0
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0

    return imgTranslasi

# Fix the file path - use forward slashes or double backslashes
image = img.imread("C:\\Users\\muham\\OneDrive\\Gambar\\534826.jpg")

imgResult = Translasi(image, shiftX=50, shiftY=-300)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.imshow(image)
plt.subplot(2,1,2)
plt.imshow(imgResult)
plt.show()