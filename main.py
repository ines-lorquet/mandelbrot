import numpy as np
import matplotlib.pyplot as plt

# appele les différentes méthodes.
from fractal import BurningShip
from fractal import Sierpinski
from fractal import Mandelbrot
from fractal import Julia


# # Sierpinski
# points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
# triangle = Sierpinski(5, points)
# triangle.draw_triangle()

# # Mandelbrot
# xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
# width, height, max_iter = 1000, 1000, 256
# mandelbrot_set = Mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
# mandelbrot_set.plot()

# Julia
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
width, height, max_iter = 1000, 1000, 256
c = complex(-0.7, 0.27015)

julia_set = Julia(c, max_iter)
julia_set.plot(xmin, xmax, ymin, ymax, width, height)




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