import matplotlib.pyplot as plt

# appele les différentes méthodes.
from fractal import BurningShip
from fractal import *


#  Crée des visualisation

# BurningShip
xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
width, height, max_iter = 1000, 1000, 256

burning_ship = BurningShip(xmin, xmax, ymin, ymax, width, height, max_iter)

X, Y, Z = burning_ship.X, burning_ship.Y, burning_ship.Z