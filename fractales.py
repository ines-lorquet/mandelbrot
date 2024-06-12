"""triangle de Sierpiński"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def midpoint(p1, p2):
    return (p1 + p2) / 2

def sierpinski_triangle(ax, level, p1, p2, p3):
    if level == 0:
        triangle = np.array([p1, p2, p3, p1])
        ax.plot(triangle[:, 0], triangle[:, 1], 'k-')
    else:
        p4 = midpoint(p1, p2)
        p5 = midpoint(p2, p3)
        p6 = midpoint(p1, p3)
        sierpinski_triangle(ax, level - 1, p1, p4, p6)
        sierpinski_triangle(ax, level - 1, p4, p2, p5)
        sierpinski_triangle(ax, level - 1, p6, p5, p3)

def draw_sierpinski_triangle(level):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3)/2])
    
    sierpinski_triangle(ax, level, p1, p2, p3)
    fig.canvas.draw_idle()

# Initialisation de la figure et de l'axe
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
ax.set_aspect('equal')
ax.axis('off')

# Initialisation du triangle de Sierpiński
initial_level = 4
draw_sierpinski_triangle(initial_level)

# Création du slider pour ajuster le niveau
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Niveau', 0, 7, valinit=initial_level, valstep=1)

# Mise à jour du triangle lorsque le slider est modifié
def update(val):
    level = slider.val
    draw_sierpinski_triangle(level)

slider.on_changed(update)

plt.show()

"""flocon de neige de Koch"""

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider

# def koch_snowflake(order, scale=10):
#     def koch_snowflake_complex(order):
#         if order == 0:
#             # Initial equilateral triangle
#             angles = np.array([0, 2*np.pi/3, 4*np.pi/3])
#             return scale * np.exp(1j * angles)
#         else:
#             Z = koch_snowflake_complex(order - 1)
#             Z_new = np.empty(len(Z) * 4, dtype=complex)
#             for i in range(len(Z)):
#                 Z_new[4*i] = Z[i]
#                 Z_new[4*i+1] = Z[i] + (Z[(i+1) % len(Z)] - Z[i]) / 3
#                 Z_new[4*i+2] = Z[i] + (Z[(i+1) % len(Z)] - Z[i]) / 3 * (1 + 1j * np.sqrt(3)) / 2
#                 Z_new[4*i+3] = Z[i] + 2 * (Z[(i+1) % len(Z)] - Z[i]) / 3
#             return Z_new

#     points = koch_snowflake_complex(order)
#     return np.real(points), np.imag(points)

# def update(val):
#     order = int(slider.val)
#     x, y = koch_snowflake(order)
#     line.set_data(np.append(x, x[0]), np.append(y, y[0]))
#     fig.canvas.draw_idle()

# # Initial plot
# initial_order = 0
# x, y = koch_snowflake(initial_order)

# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.2)
# ax.set_aspect('equal')
# line, = plt.plot(np.append(x, x[0]), np.append(y, y[0]), 'b-')

# # Slider for controlling the order of the Koch snowflake
# ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
# slider = Slider(ax_slider, 'Order', 0, 6, valinit=initial_order, valstep=1)

# slider.on_changed(update)

# plt.show()

"""burning ship"""

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# def burning_ship(c, max_iter):
#     z = np.zeros(c.shape, dtype=np.complex128)
#     mask = np.ones(c.shape, dtype=bool)
#     output = np.zeros(c.shape, dtype=int)
    
#     for i in range(max_iter):
#         z[mask] = (np.abs(z[mask].real) + 1j * np.abs(z[mask].imag))**2 + c[mask]
#         mask = np.abs(z) < 2
#         output += mask
#     return output

# def create_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
#     r1 = np.linspace(xmin, xmax, width)
#     r2 = np.linspace(ymin, ymax, height)
#     c = r1 + r2[:, None] * 1j
#     return burning_ship(c, max_iter)

# fig, ax = plt.subplots()

# xmin, xmax, ymin, ymax = -2, 1.5, -2, 1.5
# width, height = 800, 800
# max_iter = 256

# img = ax.imshow(create_fractal(xmin, xmax, ymin, ymax, width, height, max_iter), extent=[xmin, xmax, ymin, ymax], cmap='hot')
# ax.set_title("Burning Ship Fractal")

# def animate(i):
#     global xmin, xmax, ymin, ymax
#     zoom_factor = 0.9
#     xcenter = (xmin + xmax) / 2
#     ycenter = (ymin + ymax) / 2
#     xwidth = (xmax - xmin) * zoom_factor
#     yheight = (ymax - ymin) * zoom_factor
#     xmin = xcenter - xwidth / 2
#     xmax = xcenter + xwidth / 2
#     ymin = ycenter - yheight / 2
#     ymax = ycenter + yheight / 2

#     img.set_data(create_fractal(xmin, xmax, ymin, ymax, width, height, max_iter))
#     img.set_extent([xmin, xmax, ymin, ymax])
#     return [img]

# ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=True)
# plt.show()
