import numpy as np
import matplotlib.pyplot as plt

def koch_snowflake(order, scale=10):
    def koch_snowflake_complex(order):
        if order == 0:
            return np.array([0.0 + 0.0j, 1.0 + 0.0j, 0.5 + np.sqrt(3)/2*1j, 0.0 + 0.0j])
        else:
            z = koch_snowflake_complex(order - 1)
            z1 = np.roll(z, shift=-1)
            dz = z1 - z
            new_points = np.vstack([z, z + dz/3, z + dz/3 + dz/3*np.exp(np.pi*1j/3), z + 2*dz/3]).T
            return new_points.flatten()

    points = koch_snowflake_complex(order) * scale
    return points.real, points.imag

x, y = koch_snowflake(order=4)
plt.plot(x, y)
plt.axis('equal')
plt.show()
