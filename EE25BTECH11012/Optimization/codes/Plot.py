import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 10, 20)
z = np.linspace(0, 10, 20)
Y, Z = np.meshgrid(y, z)

# The boundary is x = y + z
X = Y + Z

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

# Labeling
ax.set_xlabel('Amount of X (Material 1)')
ax.set_ylabel('Amount of Y (Material 2)')
ax.set_zlabel('Amount of Z (Material 3)')
ax.set_title('Boundary Plane: x = 0.5(x + y + z)')

plt.show()