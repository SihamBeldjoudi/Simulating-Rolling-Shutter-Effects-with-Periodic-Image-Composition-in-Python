**"Simulating Rolling Shutter Effects with Periodic Image Composition in Python"**

### Project Description

This project recreates the *rolling shutter effect* in a composite image by arranging multiple image slices in a sequential, periodic pattern. Inspired by the effect seen when camera sensors capture scenes line-by-line (e.g., smartphone and DSLR video modes), this code creates a distorted appearance similar to what occurs in rolling shutter photography. By dividing an empty image matrix into row blocks and systematically inserting sections from a series of input images, we achieve a composite that echoes the motion-distorted look produced by rolling shutters.

In real-world rolling shutter effects, motion during line-by-line capture creates a staggered image where each line may slightly differ due to changes in the scene. This project emulates that effect by inserting rows from different images in a periodic arrangement across the final matrix. The result is a striking composite image that captures sequential "snapshots" across multiple input images, rendering a static yet dynamic visual.

### Key Features

- **Simulated Rolling Shutter Effect**: Creates an effect similar to rolling shutter distortions by dividing the image matrix into line segments from multiple images and organizing them periodically.
- **Flexible Image Composition**: Parameters like the frequency of image changes, resolution, and number of periods allow customizable configurations to suit different artistic and visual effects.
- **Mosaic and Art Applications**: This code can be used for creative mosaics or as a tool for analyzing patterns across image sequences, ideal for visual studies in digital art and photography.

### How It Works

1. **Load and Prepare Images**: A series of images are loaded and converted to RGB format as NumPy arrays, each representing a distinct visual source.
  
2. **Initialize the Matrix**: An empty 512x512-pixel matrix is created to hold the final composite, with color channels for RGB values.

3. **Compose the Image**:
   - The matrix is divided into several periods, each containing a fixed number of lines.
   - For each period, slices of rows from each image are inserted sequentially into the matrix. This creates periodic repetitions of different images along the vertical axis, generating a rolling shutter-inspired pattern.
  
4. **Visualize the Result**: The resulting matrix is displayed using `matplotlib` to show the final composite image, capturing the effect of dynamic visual snapshots.

### Example Use Cases

- **Artistic Mosaic Creation**: Generate mosaics that deconstruct visual data across a series of images for a unique blended artwork.
- **Rolling Shutter Effect Simulation**: Experiment with visual effects resembling motion distortions seen in rolling shutter photography.
- **Pattern Analysis**: Explore visual patterns within a series of images by overlaying segments in a periodic fashion.

### Technical Highlights

- **Rolling Shutter Simulation**: Sequential row-wise composition simulates rolling shutter by mimicking staggered visual shifts across images.
- **Customizable Parameters**: Adjustable parameters (`N`, `per`, `nbre_images_utilisees`) allow for easy customization of output size, frequency, and composition.
- **Efficient Processing**: The project uses `NumPy` for efficient matrix manipulation and `PIL` for image handling, making it suitable for larger image sets.

This project is ideal for digital artists, photographers, and technologists interested in creating visual effects that explore the principles of rolling shutters and periodic image manipulation. It offers a hands-on approach to producing complex, layered visuals from simple sequential images.
