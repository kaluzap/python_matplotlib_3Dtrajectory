#Script to generate a 3D figure

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


style.use('fivethirtyeight')

#it reads the 3d data with the trajectory                      
w, wi, er = np.loadtxt('evolution.dat', delimiter=' ', usecols = (3, 4, 5), unpack=True )

#it reads the 3d parabola
x, y, z = np.loadtxt('parabola.dat', delimiter=' ', usecols = (0, 1, 2), unpack=True )


fig = plt.figure()
ax = plt.axes(projection='3d')

#Coordinate of the target point with a blue dot.
x0 = [0,0]
y0 = [0,0]
z0 = [0,0]
ax.plot(x0, y0 ,z0, 'bo')

#Coordinate of the Initial condition with a red dot.
xi = [-3.104543]
yi = [3.519298]
zi = [9.879793]
ax.plot(xi, yi ,zi, 'bo', color = 'red')

#Drawing the parabola
ax.plot(x, y, z, linestyle = '--', color = 'blue', linewidth=0.75)

#Drawing the trajectory
ax.plot(w, wi, er,color = 'black', linewidth=0.75)

#Labeling
ax.set_xlabel(r'$w$')
ax.set_ylabel(r"$w$'")
ax.zaxis.set_rotate_label(False)    #it allows to rotate the label!
ax.set_zlabel(r"$\epsilon'$", rotation=0)
ax.tick_params(labelsize=10)    #resizing the numbers

#Setting the box size
ax.set_xlim(-4.0, 4.0)
ax.set_ylim(-4.0, 4.0)
ax.set_zlim(0.0, 10.0)


plt.savefig('trajectory.png', bbox_inches='tight')

plt.show()
