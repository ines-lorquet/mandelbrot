import numpy as np
import matplotlib.pyplot as plt

# appele les différentes classes.
from fractal import BurningShip
from fractal import Sierpinski
from fractal import Mandelbrot
from fractal import Julia
from fractal import Koch


# AJOUTER UN PROMPT QUI DEMANDE A L'UTILISATEUR DE CHOISIR UNE FIGURE FRACTALE

# # Sierpinski
# points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
# triangle = Sierpinski(5, points)
# triangle.draw_triangle()

# # Mandelbrot
# xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
# width, height, max_iter = 1000, 1000, 256
# mandelbrot_set = Mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
# mandelbrot_set.plot()

# # Julia
# xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
# width, height, max_iter = 1000, 1000, 256
# c = complex(-0.7, 0.27015)
# julia_set = Julia(c, max_iter)
# julia_set.plot(xmin, xmax, ymin, ymax, width, height)


# # Koch
# koch_snowflake = Koch(order=4)
# koch_snowflake.plot()

# BurningShip
xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
width, height, max_iter = 1000, 1000, 256

burning_ship = BurningShip(xmin, xmax, ymin, ymax, width, height, max_iter)

X, Y, Z = burning_ship.X, burning_ship.Y, burning_ship.Z








# #  Crée des visualisation
# sort = int(input("\nChoose the number corresponding to the desired fractal : "))

# # Mapping the sort methods and their corresponding classes
# sorting_methods = {
#     1: (Sierpinski, "Sierpinski"),
#     2: (Mandelbrot, "Mandelbrot"),
#     3: (Insertion, "insertion sort"),
#     4: (Fusion, "merge sort"),
#     5: (Quick, "quick sort"),
#     6: (Heap, "heap sort"),
#     7: (BurningShip, "BurningShip")
# }