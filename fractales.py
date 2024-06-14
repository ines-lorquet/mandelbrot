import numpy as np
import matplotlib.pyplot as plt

class Fractals:
    def __init__(self, fractal_type, **kwargs):
        self.fractal_type = fractal_type
        self.kwargs = kwargs

    def draw(self):
        
        if self.fractal_type == 'sierpinski':
            self._draw_sierpinski()
        elif self.fractal_type == 'mandelbrot':
            self._draw_mandelbrot()
        elif self.fractal_type == 'julia':
            self._draw_julia()
        elif self.fractal_type == 'koch':
            self._draw_koch()
        elif self.fractal_type == 'burning_ship':
            self._draw_burning_ship()
        else:
            raise ValueError("Unknown fractal type")

    def _draw_sierpinski(self):
        order = self.kwargs['order']
        points = self.kwargs['points']
        self._sierpinski_triangle(order, points)
        
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
    
    def _draw_mandelbrot(self):
        self._mandelbrot_set(self.kwargs)

    def _mandelbrot(self, c, max_iter):
        z = c
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z * z + c
        return max_iter

    def _mandelbrot_set(self, kwargs):
        xmin, xmax, ymin, ymax = kwargs['xmin'], kwargs['xmax'], kwargs['ymin'], kwargs['ymax']
        width, height, max_iter = kwargs['width'], kwargs['height'], kwargs['max_iter']
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        Z = np.array([[self._mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])
        plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
        plt.colorbar()

    def _draw_julia(self):
        self._julia_set(self.kwargs)

    def _julia(self, z, c, max_iter):
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z * z + c
        return max_iter

    def _julia_set(self, kwargs):
        c = kwargs['c']
        xmin, xmax, ymin, ymax = kwargs['xmin'], kwargs['xmax'], kwargs['ymin'], kwargs['ymax']
        width, height, max_iter = kwargs['width'], kwargs['height'], kwargs['max_iter']
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        Z = np.array([[self._julia(complex(r, i), c, max_iter) for r in r1] for i in r2])
        plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
        plt.colorbar()

    def _draw_koch(self):
        self._koch_snowflake(self.kwargs)

    def _koch_snowflake_complex(self, order):
        if order == 0:
            return np.array([0.0 + 0.0j, 1.0 + 0.0j, 0.5 + np.sqrt(3)/2*1j, 0.0 + 0.0j])
        else:
            z = self._koch_snowflake_complex(order - 1)
            z1 = np.roll(z, shift=-1)
            dz = z1 - z
            new_points = np.vstack([z, z + dz/3, z + dz/3 + dz/3*np.exp(np.pi*1j/3), z + 2*dz/3]).T
            return new_points.flatten()

    def _koch_snowflake(self, kwargs):
        order = kwargs['order']
        scale = kwargs.get('scale', 10)
        points = self._koch_snowflake_complex(order) * scale
        x, y = points.real, points.imag
        plt.plot(x, y)
        plt.axis('equal')

    def _draw_burning_ship(self):
        self._burning_ship_set(self.kwargs)

    def _burning_ship(self, c, max_iter):
        z = c
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = complex(abs(z.real), abs(z.imag))**2 + c
        return max_iter

    def _burning_ship_set(self, kwargs):
        xmin, xmax, ymin, ymax = kwargs['xmin'], kwargs['xmax'], kwargs['ymin'], kwargs['ymax']
        width, height, max_iter = kwargs['width'], kwargs['height'], kwargs['max_iter']
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        Z = np.array([[self._burning_ship(complex(r, i), max_iter) for r in r1] for i in r2])
        plt.imshow(Z, extent=[xmin, xmax, ymin, ymax])
        plt.colorbar()