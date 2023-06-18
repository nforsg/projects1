from func_mania import Pasture
from func_mania import Functions



arr1 = [1,2,3,4,5,6,7,8]
arr2 = [10,9,8,7,6,5,4,3,2,1]
func = Functions()
pst = Pasture()

def test_size_functions():
    '''Testig the array-size function called counter in class Functions'''
    
    assert func.counter(arr1) == len(arr1)
    
    assert func.counter(arr2) == len(arr2) 

def test_sort_functions():
    '''Testing the mergesort in class Functions'''
   
    for i in range(1, len(arr1)):
        assert func.mergesort(arr1)[i-1] <= func.mergesort(arr1)[i]
    
    for j in range(1, len(arr2)):
        assert func.mergesort(arr2)[j-1] <= func.mergesort(arr2)[j]

def test_pasture():
    '''Testing funcitonality of Pasture class'''

    assert pst.counter() == 0

    pst.add_animal(10,10, 'Cow', 15, 15)
    assert pst.land[10,10] == 2

    pst.add_animal(20,20, 'Sheep', 8,8)
    assert pst.land[20,20] == 1
    
    pst.add_animal(18,18, 'Bull', 12,12)
    assert pst.land[18,18] == 6

    pst.counter() == 3