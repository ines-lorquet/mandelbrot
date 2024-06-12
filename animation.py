import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Parameters
x_start, y_start = -2, -1.5  # an interesting region starts here
width, height = 3, 3  # for 3 units up and right
density_per_unit = 100  # reduced density for faster computation

# Real and imaginary axis
re = np.linspace(x_start, x_start + width, width * density_per_unit)
im = np.linspace(y_start, y_start + height, height * density_per_unit)
RE, IM = np.meshgrid(re, im)
C = RE + 1j * IM

# Define the vectorized Mandelbrot function
def mandelbrot(c, max_iter):
    z = np.zeros(c.shape, dtype=complex)
    div_time = np.zeros(c.shape, dtype=int)
    mask = np.ones(c.shape, dtype=bool)
    
    for i in range(max_iter):
        z[mask] = z[mask] ** 2 + c[mask]
        mask = np.abs(z) <= 2
        div_time[mask] = i
    return div_time

# Generate and save the images
for frame in range(45):
    print(f"Generating frame {frame}")
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.set_xticks([])  # clear x-axis ticks
    ax.set_yticks([])  # clear y-axis ticks
    
    threshold = round(1.15**(frame + 1))
    X = mandelbrot(C, threshold)
    
    ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    plt.savefig(f'mandelbrot_{frame}.png')
    plt.close(fig)

# Create the GIF
print("Creating GIF")
images = [Image.open(f'mandelbrot_{frame}.png') for frame in range(45)]
images[0].save('mandelbrot.gif', save_all=True, append_images=images[1:], duration=120, loop=0)

# Clean up the individual PNG files
import os
for frame in range(45):
    os.remove(f'mandelbrot_{frame}.png')

print("Completed")
