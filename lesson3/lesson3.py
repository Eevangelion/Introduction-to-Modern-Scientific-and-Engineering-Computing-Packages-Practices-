import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import seaborn as sns
from locale import normalize
ax = axes3d.Axes3D(plt.figure())
# or
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

x = y = np.linspace(-3, 3, 74)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(4*R)/R
fig, ax = plt.subplots(1, 3, figsize=(14, 4), subplot_kw=dict(projection='3d'))

p = ax[0].plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap=mpl.cm.inferno)
cb = fig.colorbar(p, ax=ax[0], shrink=0.6)

ax[0].set_xlabel("$x$", fontsize=16)
ax[0].set_ylabel("$y$", fontsize=16)
ax[0].set_zlabel("$z$", fontsize=16)

ax[1].plot_wireframe(X, Y, Z, rstride=3, cstride=3, cmap=mpl.cm.inferno)
ax[1].set_title("plot wireframe")

ax[2].contour(X, Y, Z, zdir='z', offset=0, cmap=mpl.cm.inferno)
ax[2].set_title("contour")

ax[2].set_xlabel("$x$", fontsize=16)
ax[2].set_ylabel("$y$", fontsize=16)
ax[2].set_zlabel("$z$", fontsize=16)

# mgrid транспонирует матрицу, т.е. x, y = y, x
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = 4*np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', ylim=(-4, 4), zlim=(-4, 4))
ax.plot_surface(x, y, z, cmap='inferno')

ax.legend()
plt.show()
