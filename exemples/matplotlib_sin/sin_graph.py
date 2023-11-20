import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time  # Importez la bibliothèque time

# Paramètres de la sinusoïde
freq = 2  # fréquence
amplitude = 1  # amplitude

# Créer une figure et un axe
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

start_time = time.time()

# Initialiser l'axe
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-amplitude * 1.1, amplitude * 1.1)
    return ln,

# Fonction de mise à jour de l'animation
def update(frame):
    # Délais pour me laisser le temps de faire une capture d'écran
    current_time = time.time()
    # Vérifier si 2 secondes se sont écoulées
    if current_time - start_time < 2:
        return ln,
    
    xdata.append(frame)
    ydata.append(amplitude * np.sin(freq * frame))
    ln.set_data(xdata, ydata)
    return ln,

# Créer l'animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 64),
                    init_func=init, blit=True)

# Afficher l'animation
plt.show()
