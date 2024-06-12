import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height, max_iter = 1000, 1000, 256

X, Y, Z = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.show()
