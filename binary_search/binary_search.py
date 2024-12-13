


def bs(arr, target):
    low = 0
    high = len(arr)-1


    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

        
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = bs(arr, x)
        



