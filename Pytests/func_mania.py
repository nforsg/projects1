import  numpy as np
import random as rn

class _Animal():
    def __init__(self, species, mood, hunger, health, diet):
        self.species = species
        self.mood = mood
        self.hunger = hunger
        self.health = health
        self.diet = diet

class Pasture():
    def __init__(self, land = np.zeros((100,100)), temperature = 25):
        self.land = land
        self.temp = temperature

    def counter(self, array):

        '''Counting the number of animals in the pasture'''
        
        count = 0
        for i in range(np.shape(self.land)[0]):
            for j in range(np.shape(self.land)[1]):
                if self.land[i,j] != 0:
                    count += 1
        return count
    
    #def add_animal(x,y, species, mood, hunger, health, diet):
        





    def mergesort(self, array):
        '''Sorts the array with divide & conquer in O(nlogn) time'''
        if len(array) > 1:
            splitter_index = len(array)//2
            left_part = array[:splitter_index]
            right_part = array[splitter_index:]

            self.mergesort(left_part)
            self.mergesort(right_part)

            left_idx = 0
            right_idx = 0
            merge_idx = 0

            while left_idx < len(left_part) and right_idx < len(right_part):
                if left_part[left_idx] < right_part[right_idx]:
                    array[merge_idx] = left_part[left_idx]
                    left_idx += 1
                else: 
                    array[merge_idx] = right_part[right_idx]
                    right_idx += 1
                merge_idx += 1

            while left_idx < len(left_part):
                array[merge_idx] = left_part[left_idx]
                left_idx += 1
                merge_idx += 1

            while right_idx < len(right_part):
                array[merge_idx] = right_part[right_idx]
                right_idx += 1
                merge_idx += 1 
        return array
        
