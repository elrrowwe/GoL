import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = int(input('Welcome to Conway`s Game of Life! Please, enter the size of the simulation(NxN):'))
size = (N, N)
proba_0 = 0.8                 # resulting array will have 80% of zeros
sim = np.random.choice([0, 1], size=size, p=[proba_0, 1 - proba_0])
nsim = np.copy(sim)

fig, ax = plt.subplots(figsize=(5, 5))
im = ax.imshow(sim, aspect='equal', cmap='summer', animated=True)
im.set_clim(vmin=0, vmax=1)

def update(i):
    for l in range(N):
        for m in range(N):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (l + i >= 0 and l + i < N) and (m + j >= 0 and m + j < N): #check whether the index is out of range
                        neighbors += nsim[l + i][m + j]

            neighbors -= nsim[l][m] #subtract the current cell, since it was counted in as well

            if nsim[l, m] == 1:
                if neighbors == 2 or neighbors == 3:
                    pass
                if neighbors < 2 or neighbors > 3:
                    nsim[l, m] = 0
            elif nsim[l, m] == 0:
                if neighbors == 3:
                    nsim[l, m] = 1
                else:
                    pass
    im.set_data(nsim)
    return im,

ani = animation.FuncAnimation(fig, update, interval=5, frames=4000, blit=True)
plt.axis('off')
plt.draw()
plt.show()
