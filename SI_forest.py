#Código en python para visualizar la propagación de un a enfermedad 
#Se tienen los estados S,I, se agregó el estado vacío como en incendios forestales
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors


neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))
E, S, I = 0, 1, 2

colors_list = ["gray", "lawngreen", "gray","darkorange" ]
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3]
norm = colors.BoundaryNorm(bounds, cmap.N)

def iterate(X):
    X1 = np.zeros((nx, ny))
    for ix in range (1,nx-1):
        for iy in range (1,ny-1):
            if X[iy,ix] == E:
                continue
            elif X[iy,ix]==I:
                X1[iy,ix] = I
            else:
                X1[iy,ix] = S
                for dx,dy in neighbourhood:
                     if X[iy+dy,ix+dx] == I:
                        X1[iy,ix] = I
                        break            
    return X1

# "Densidad" poblacional
forest_fraction = 0.5
# # Proba
# p, f = 0.1, 0.1
# # Forest size (number of cells in x and y directions).
nx, ny = 100, 100
# Initialize the forest grid.
X  = np.zeros((ny, nx))
X[1:ny-1, 1:nx-1] = np.random.randint(0, 2, size=(ny-2, nx-2))
X[1:ny-1, 1:nx-1] = np.random.random(size=(ny-2, nx-2)) < forest_fraction
X[50,50]=2

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)#, interpolation='nearest')

# The animation function: called to produce a frame for each generation.
def animate(i):
    im.set_data(animate.X)
    animate.X = iterate(animate.X)
# Bind our grid to the identifier X in the animate function's namespace.
animate.X = X
#print(np.count_nonzero(X == 2))
# Interval between frames (ms).
interval = 100
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)
plt.show()
