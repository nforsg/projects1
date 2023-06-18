from func_mania import Pasture



arr1 = [1,2,3,4,5,6,7,8]
arr2 = [10,9,8,7,6,5,4,3,2,1]
func = Pasture()

def test_size():
    '''Testig the array-size function called counter'''
    
    assert func.counter(arr1) == len(arr1)
    
    assert func.counter(arr2) == len(arr2) 

def test_sort():
    '''Testing the mergesort'''
   
    for i in range(1, len(arr1)):
        assert func.mergesort(arr1)[i-1] <= func.mergesort(arr1)[i]
    
    for j in range(1, len(arr2)):
        assert func.mergesort(arr2)[j-1] <= func.mergesort(arr2)[j]

