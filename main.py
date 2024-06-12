import numpy as np
import matplotlib.pyplot as plt

from fractales import BurningShip, Sierpinski, Mandelbrot, Julia, Koch

def main():
    # display the fractale figures available
    print("1. Sierpinski")
    print("2. Mandelbrot")
    print("3. Julia")
    print("4. Koch")
    print("5. BurningShip")

    # Ask the user to choose a fractal
    figure = int(input("\nChoose the number corresponding to the desired fractal figure : "))

    # Mapping of the fractal figures and their corresponding classes
    fractal_figures = {
        1: (Sierpinski, "Sierpinski"),
        2: (Mandelbrot, "Mandelbrot"),
        3: (Julia, "Julia"),
        4: (Koch, "Koch"),
        5: (BurningShip, "BurningShip")
    }


    # Instanciate the chosen fractal figure
    if figure == 1:
        # Sierpinski
        points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
        sierpinski_triangle = Sierpinski(order=5, points=points)
        sierpinski_triangle.draw_triangle()
    elif figure == 2:
        # Mandelbrot
        xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
        width, height, max_iter = 1000, 1000, 256
        mandelbrot_set = Mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
        mandelbrot_set.plot()
    elif figure == 3:
        # Julia
        xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
        width, height, max_iter = 1000, 1000, 256
        c = complex(-0.7, 0.27015)
        julia_set = Julia(c, max_iter)
        julia_set.plot(xmin, xmax, ymin, ymax, width, height)
    elif figure == 4:
        # Koch
        koch_snowflake = Koch(order=4)
        koch_snowflake.plot()
    elif figure == 5:
        # BurningShip
        xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
        width, height, max_iter = 1000, 1000, 256
        burning_ship = BurningShip(xmin, xmax, ymin, ymax, width, height, max_iter)
        burning_ship.plot()
    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")

if __name__ == "__main__":
    main()





# # # BurningShip
# # xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
# # width, height, max_iter = 1000, 1000, 256

# # burning_ship = BurningShip(xmin, xmax, ymin, ymax, width, height, max_iter)

# # X, Y, Z = burning_ship.X, burning_ship.Y, burning_ship.Z








