import numpy as np
import matplotlib.pyplot as plt

def julia(c, max_iter):
    def f(z):
        return z*z + c

    def divergence(z):
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = f(z)
        return max_iter

    return divergence

def julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[julia(c, max_iter)(complex(r, i)) for r in r1] for i in r2]))

xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
width, height, max_iter = 1000, 1000, 256
c = complex(-0.7, 0.27015)

X, Y, Z = julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter)

plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.show()
