import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Création de la figure et de l'axe
fig, ax = plt.subplots()
x_data = np.linspace(0, 4 * np.pi, 100)
line, = ax.plot(x_data, np.sin(x_data))

# Fonction pour mettre à jour le graphique à chaque itération
def update(frame):
    line.set_data(x_data + frame * 0.1, np.sin(x_data))
    return line,

# Création de l'animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

# Affichage de l'animation
plt.show()
