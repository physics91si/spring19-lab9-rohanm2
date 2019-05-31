# Physics 91SI
# Spring 2019
# Lab 9

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle

# TODO: Implement this function
def init_molecule():
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them""" 
    p1 = Particle(5, 6) 
    p2 = Particle(5, 6) 
    mol = Molecule(p1.pos, p1.m, p2.pos, p2.m, 3, 4)  
    return mol 


# TODO: Implement this function
def time_step(dt, mol): 
    """Sets new positions and velocities of the particles attached to mol"""
    pass


#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
