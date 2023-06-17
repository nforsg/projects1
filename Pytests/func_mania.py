import  numpy as np

class Functions():
    def __init__(self):
        pass

    def counter(self, array):
        
        count = 0
        for i in range(len(array)):
            count += 1
        return count

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
        
