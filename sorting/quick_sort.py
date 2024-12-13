

# def partition(array, low, high):

#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         print(j)

#         if array[j] <= pivot:
#             i += 1

#             array[i], array[j] = array[j], array[i]
    
#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1


# def quick_sort(array, low, high):
#     if low < high:
           
#         pivot_index = partition(array, low, high)

#         quick_sort(array, 0, pivot_index-1)
#         quick_sort(array, pivot_index+1, high)


def quick_sort(arr):

    if len(arr) <= 1:

        return arr

    else:

        pivot = arr[0]
        left = []
        right = []
        
        for i in array[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)

        return quick_sort(left) + [pivot] + quick_sort(right)

array = [12, 12, 10, 9, 8]
# quick_sort(array, 0, len(array)-1)
quick_sort(array)

print(array)

