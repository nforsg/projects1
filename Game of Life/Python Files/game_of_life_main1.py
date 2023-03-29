import numpy as np
import time
from matplotlib import pyplot as plt
import pygame as pg
from random import random as rnd

BG_COLOR = (10, 10, 10) #Background color
COLOR_GRID = (40,40,40) #Grid color
COLOR_DIE_NEXT = (250, 25 ,25)
PREDATOR_COLOR = (10, 10, 200) #PREDATOR COLOR (red)
OMNIVORE_COLOR = (200, 10, 200) #OMNIVORE COLOR (purple)
HERBAVORE_COLOR = (25, 255, 25) #HERBAVORE COLOR (green)

class Predators:
    def __init__(self, energy_state, P_p, energy_magnitude, n_p, m_p_o, energy_decrease_n, energy_decrease_m, energy_increase_s):
        self.energy_state = energy_state
        self.P_p = P_p
        self.energy_magnitutde = energy_magnitude
        self.m_p_o = m_p_o
        self.n_p = n_p
        self.energy_decrease_n = energy_decrease_n
        self.energy_decrease_m = energy_decrease_m
        self.energy_increase_s = energy_increase_s
    
class Omnivores:
    def __init__(self, P_o, n_o, m_o, m_o_h):
        self.P_o = P_o
        self.n_o = n_o
        self.m_o = m_o
        self.m_o_h = m_o_h

class Herbivores:
    def __init__(self, P_h, n_h):
        self.P_h = P_h
        self.n_h = n_h

class Simulation:
    def __init__(self, screen, size1, size2, cells, size, predator, omnivore, herbivore, with_progress = False):
        self.screen = screen
        self.size1 = size1
        self.size2 = size2
        self.cells = cells
        self.size = size
        self.with_progress = with_progress
    
    def counter(self, array):
        predator_number = 0
        omnivore_number = 0
        herivore_number = 0
        for row, col in np.ndindex(array.shape):
            if array[row, col] == 1:
                predator_number += 1
            elif array[row, col] == 2:
                omnivore_number += 1
            elif array[row, col] == 3:
                herbavore_number += 1
            else:
                continue
        return predator_number, omnivore_number, herbavore_number
    
    def timestep(self)

