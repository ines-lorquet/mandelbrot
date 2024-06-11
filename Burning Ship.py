import numpy as np
import matplotlib.pyplot as plt

def burning_ship(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = complex(abs(z.real), abs(z.imag))**2 + c
    return max_iter

def burning_ship_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[burning_ship(complex(r, i), max_iter) for r in r1] for i in r2]))

xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
width, height, max_iter = 1000, 1000, 256

X, Y, Z = burning_ship_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.show()
