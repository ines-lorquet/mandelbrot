import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(order, points):
    if order == 0:
        plt.fill(points[:, 0], points[:, 1], 'b')
    else:
        mid1 = (points[0] + points[1]) / 2
        mid2 = (points[1] + points[2]) / 2
        mid3 = (points[2] + points[0]) / 2
        sierpinski_triangle(order-1, np.array([points[0], mid1, mid3]))
        sierpinski_triangle(order-1, np.array([points[1], mid1, mid2]))
        sierpinski_triangle(order-1, np.array([points[2], mid2, mid3]))

points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
sierpinski_triangle(5, points)
plt.gca().set_aspect('equal')
plt.show()
