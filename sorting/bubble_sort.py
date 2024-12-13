

def  bubble_sort(array):
    
    n = len(array)

    while (n > 0):

        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        
        n -=1
    return array

a = [1,3,2,4,6,5,7,9,8]
print(bubble_sort(a))

    
