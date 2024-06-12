import numpy as np


# Prend les fichiers burning ship, julia, mandelbrot, Sierpinsky et Koch pour en faire des classes.
class Julia:
    pass

class Mandelbrot:
    pass

class Sierpinsky:
    pass

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


