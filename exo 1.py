import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définir les paramètres de la courbe
r = 1  # Rayon du cercle de base
u = np.linspace(0, 2*np.pi, 100)  # Valeurs de u
v = np.linspace(-1, 1, 100)  # Valeurs de v

# Créer les coordonnées x, y, z en fonction des paramètres
U, V = np.meshgrid(u, v)
x = r * np.cos(U)
y = r * np.sin(U)
z = V

# Tracer le cylindre
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha=0.5)

# Tracer le cône
ax.plot_surface(x, y, z, color='white', alpha=0.2)
ax.plot_surface(x, y, -z, color='black', alpha=1.0)

# Paramètres d'affichage
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1, 1)
plt.show()
