# Physics 91SI
# Spring 2019
# Lab 9

import numpy as np

class Molecule:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, pos1, m1, pos2, m2, K, L0):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.p1 = Particle(pos1, m1) 
        self.p2 = Particle(pos2, m2) # Sets x position 
        self.k = K 
        self.l0 = L0 
    
    def get_displ(): 
        return pos2 - pos1 
        
    def get_force(): 
        force = k * (pos2 - pos1 - l0) 
        return force 
        
        # force = k(x2 - x1 - l0) 
         
mol = Molecule(1, 2, 3, 1, 5, 6) 
print(mol.get_force) 

    