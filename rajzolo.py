import numpy as np
import matplotlib.pyplot as plt



def printact(x, y, xrange=1):
    fig, ax = plt.subplots()
    ax.plot(x, y, lw=3, c='darkblue')

    # Tengelyek középre helyezése
    ax.spines['left'].set_position('zero')  # Y tengely középre
    ax.spines['bottom'].set_position('zero')  # X tengely középre

    # A többi tengely eltávolítása
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Ticks helyeinek beállítása
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Azonos skálák beállítása mindkét tengelyen (hogy szimmetrikus legyen a középen)
    ax.set_xlim(-xrange, xrange)
    ax.set_ylim(-2, 2)
    
    plt.show()



def printrelu(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, lw=3, c='darkred')

    # Tengelyek középre helyezése
    ax.spines['left'].set_position('zero')  # Y tengely középre
    ax.spines['bottom'].set_position('zero')  # X tengely középre

    # A többi tengely eltávolítása
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Ticks helyeinek beállítása
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Azonos skálák beállítása mindkét tengelyen (hogy szimmetrikus legyen a középen)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    plt.show()



def printrelugame(x, y):
    fig, ax = plt.subplots()
    
    ax.plot(x, y, c='red', lw=4)
    ax.plot(x, np.sin(x*6), c='green')
    ax.set_xlim((-0.1, 1.1))
    ax.set_ylim((-1.2, 1.2))
    
    plt.show()

