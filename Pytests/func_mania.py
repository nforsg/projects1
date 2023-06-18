import  numpy as np
import random as rn

class _Animal():
    def __init__(self, species, mood, hunger):#, health, diet):
        self.species = species
        self.mood = mood
        self.hunger = hunger
        #self.health = health
        #self.diet = diet

class Pasture():
    '''Class that represents a pasture, filled with animals'''
    def __init__(self, land = np.zeros((25,25)), temperature = 25):

        '''Initialiizng properties of pasture'''

        self.land = land
        self.temp = temperature

    def counter(self):

        '''Counting the number of animals in the pasture'''

        count = 0
        for i in range(np.shape(self.land)[0]):
            for j in range(np.shape(self.land)[1]):
                if self.land[i,j] != 0:
                    count += 1
        return count
    
    def add_animal(self, x,y, species, mood, hunger):#, health, diet):

        '''Adding amnimal to the pasture'''

        anm = _Animal(species, mood, hunger)#, health, diet)
        if anm.species == "Sheep":
            self.land[x,y] = 1

        elif anm.species == "Cow":
            self.land[x,y] = 2

        elif anm.species == "Lama":
            self.land[x,y] == 3
        
        elif anm.species == "Bull":
            self.land[x,y] = 6

        else:
            print('Not a valid species of animal')

        if anm.mood in range(10):
            if anm.hunger in range(10):
                print('The ', anm.species, ' is in a bad mood due to hunger.')
            else: 
                print('The ', anm.species, ' is in a bad mood due to the weather')
        else: 
            print('The ', anm.species , ' is doing fine and is in a good mood.')
        
        print(self.land)

        return self.land
    

class Functions(): 
    def __init__(self) -> None:
        pass
    
    def counter(self, array): 
        
        '''Counting number of elements in array'''
        
        counter = 0

        for i in range(len(array)):
            counter += 1 
        return counter

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
        
