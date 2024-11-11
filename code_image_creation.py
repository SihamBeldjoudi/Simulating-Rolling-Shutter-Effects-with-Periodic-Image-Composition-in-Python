# Library Imports
import numpy as np                # For numerical matrix operations
import matplotlib.pyplot as plt    # For displaying images and graphs
from PIL import Image              # For handling image loading and conversion

# Image Settings
nbre_total_images = 512            # Total number of available images
nbre_images_utilisees = 512        # Number of images to actually use in the pattern

# Function to convert an image to an RGB pixel array
def image_array(filepath):
    image = Image.open(filepath).convert("RGB")  # Open the image and convert to RGB
    return np.array(image)                       # Return as a NumPy array of pixels

# Load and select images based on the number specified
images = [image_array(f'_{i*(nbre_total_images // nbre_images_utilisees)}.png') for i in range(0, nbre_images_utilisees)]

# Create an empty matrix of 512x512 pixels with 3 color channels (RGB)
Matrice_zeros = np.zeros((512, 512, 3), dtype=np.uint8)

# Matrix and Period Settings
N = 512              # Dimension of the final square matrix in pixels
per = 5              # Number of periods (segments) to divide the matrix into
n_lignes_periode = N / per                # Number of lines per period in the matrix
n_lignes_blocs = n_lignes_periode / nbre_images_utilisees  # Number of lines per image block within a period

# Loop to apply each image block in a periodic rolling shutter-like pattern
for a in range(per + 1):               # Loop through each period
    for i in range(nbre_images_utilisees):   # Loop through each image
        # Calculate the start and end indices for each block in the current period
        debut = i * n_lignes_blocs + a * n_lignes_periode
        fin = (i + 1) * n_lignes_blocs + a * n_lignes_periode
        # Insert the portion of the image into the final matrix
        Matrice_zeros[int(debut):int(fin)+1, :] = images[i][int(debut):int(fin)+1, :]

# Debug Information Output
print('Number of images used: ', nbre_images_utilisees)
print('Lines per image block: ', n_lignes_blocs)
print('Number of periods: ', per)
print('Lines per period: ', n_lignes_periode)

# Display the final matrix as an image
print(Matrice_zeros.shape)  # Prints the shape of the matrix (512, 512, 3)

# Display the generated matrix with matplotlib
plt.imshow(Matrice_zeros)   # Shows the matrix as an image
plt.axis('on')              # Display axis
plt.show()                  # Render the image in a graphical window