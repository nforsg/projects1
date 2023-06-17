import  numpy as np

class Functions():
    def __init__(self):
        self.hej = None

    def counter(self, array):
        
        count = 0
        for i in range(len(array)):
            count += 1
        return count
    
def main(): 
    arr1 = [1,2,3,4,5,6,7,8]
    func = Functions()
    assert func.counter(arr1) == 8 
    

if __name__== '__main__':
    main()