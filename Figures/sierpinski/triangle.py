import matplotlib.pyplot as plt
import numpy as np

''' Triangle

4 - - A - -
3 - - - - -
2 - - - - -
1 - - - - -
0 B - - - C
  0 1 2 3 4 

'''

# Triangle's points
points = np.array([
    [2, 4],         # Sommet A
    [0, 0],         # Sommet B
    [4, 0],         # Sommet C
    # [2, 4]          # Revenir au point de départ pour fermer le triangle
])

# point coordonates lists
x, y = points[:, 0], points[:, 1]


# Calcul de la demi-largeur
min_x = np.min(points[:, 0])
max_x = np.max(points[:, 0])
half_width = (max_x - min_x) / 2

# Calcul de la demi-hauteur
min_y = np.min(points[:, 1])
max_y = np.max(points[:, 1])
half_height = (max_y - min_y) / 2


# Fill the triangle
plt.fill(x, y, 'skyblue', edgecolor='black')

# draw the triangle
plt.plot(x, y, marker='o')

# Graphic's axes
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Graphic's title
plt.title('Triangle de Sierpinski')

# Display the grid
plt.grid(True)

# Display
plt.show()
