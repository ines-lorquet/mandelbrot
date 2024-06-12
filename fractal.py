import numpy as np
import matplotlib.pyplot as plt

# Prend les fichiers burning ship, julia, mandelbrot, Sierpinsky et Koch pour en faire des classes.
class Sierpinski:
    def __init__(self, order, points):
        self.order = order
        self.points = points

    def draw_triangle(self):
        self._sierpinski_triangle(self.order, self.points)
        plt.show()

    def _sierpinski_triangle(self, order, points):
        if order == 0:
            plt.fill(points[:, 0], points[:, 1], 'b')
        else:
            mid1 = (points[0] + points[1]) / 2
            mid2 = (points[1] + points[2]) / 2
            mid3 = (points[2] + points[0]) / 2
            self._sierpinski_triangle(order-1, np.array([points[0], mid1, mid3]))
            self._sierpinski_triangle(order-1, np.array([points[1], mid1, mid2]))
            self._sierpinski_triangle(order-1, np.array([points[2], mid2, mid3]))




class Mandelbrot:

    def __init__(self, xmin, xmax, ymin, ymax, width, height, max_iter):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.X, self.Y, self.Z = self._compute_set()

    def _mandelbrot(self, c):
        z = c
        for n in range(self.max_iter):
            if abs(z) > 2:
                return n
            z = z * z + c
        return self.max_iter

    def _compute_set(self):
        r1 = np.linspace(self.xmin, self.xmax, self.width)
        r2 = np.linspace(self.ymin, self.ymax, self.height)
        Z = np.array([[self._mandelbrot(complex(r, i)) for r in r1] for i in r2])
        return r1, r2, Z

    def plot(self):
        plt.imshow(self.Z, extent=[self.xmin, self.xmax, self.ymin, self.ymax])
        plt.colorbar()
        plt.show()





class Julia:
    def __init__(self, c, max_iter):
        self.c = c
        self.max_iter = max_iter

    def _f(self, z):
        return z * z + self.c

    def _divergence(self, z):
        for n in range(self.max_iter):
            if abs(z) > 2:
                return n
            z = self._f(z)
        return self.max_iter

    def compute_set(self, xmin, xmax, ymin, ymax, width, height):
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        Z = np.array([[self._divergence(complex(r, i)) for r in r1] for i in r2])
        return r1, r2, Z

    def plot(self, xmin, xmax, ymin, ymax, width, height):
        _, _, Z = self.compute_set(xmin, xmax, ymin, ymax, width, height)
        plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
        plt.colorbar()
        plt.show()





class Koch:
    pass

class BurningShip:
    def __init__(self, xmin, xmax, ymin, ymax, width, height, max_iter):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.X, self.Y, self.Z = self._compute_set()

    def _burning_ship(self, c):
        z = c
        for n in range(self.max_iter):
            if abs(z) > 2:
                return n
            z = complex(abs(z.real), abs(z.imag))**2 + c
        return self.max_iter

    def _compute_set(self):
        r1 = np.linspace(self.xmin, self.xmax, self.width)
        r2 = np.linspace(self.ymin, self.ymax, self.height)
        Z = np.array([[self._burning_ship(complex(r, i)) for r in r1] for i in r2])
        return r1, r2, Z


