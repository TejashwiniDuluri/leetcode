

def insertion_sort(array):

    le = len(array)
    
    for i in range(1, le):
        
        comaprision_key = array[i]
        
        prev = i-1

        while prev >=0:
            if array[prev] > comaprision_key:
                array[prev], array[i] = array[i], array[prev]
            prev -=1 
    
    return array



a = [1,3,2,4,6,5,7,9,8]
print(insertion_sort(a))

    