import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-20, 20, 0.1)
Y = np.arange(-20, 20, 0.1)
X, Y = np.meshgrid(X, Y)

R = np.round(np.sqrt(X**2+Y**2))
Z = 1000*(-0.9)**R
print(Z)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-2500, 2500)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
#ax.zaxis.set_major_forma

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=2)

plt.show()