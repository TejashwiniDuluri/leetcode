# Explanation

# [10,24,76,73]

# func([10,24,76,73]) 	=> func([10,24]) 	=> func([10]) => return 10
# 									        => func([24]) => return 24
# 									           => merge_sort(10,24) => [10,24]

# 					    => func([76,73]) 	=> func([76]) => return 76
# 									        => func([73]) => return 73
# 									        => merge_sort(76,73) => [76,73]


# 					    => merge_sort([10,24], [73,76]) => [10,24,73,76]

def divide(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = divide(array[:mid])
    right = divide(array[mid:])
    return merge_sort(left, right)


def merge_sort(left, right):
    result_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_array.append(left[i])
            i += 1
        else:
            result_array.append(right[j])
            j += 1
    result_array += left[i:]
    result_array += right[j:]
    return result_array


array = [1, 2, 3, 6, 2, 8, 10, 9]
print(divide(array))



# def  divide(array):
#     if len(array) == 1:
#         return array

#     mid = len(array)//2

#     left = divide(array[:mid])
#     right = divide(array[mid:])

#     return merge_sort(left, right)


# def merge_sort(left, right):

#     i, j= 0, 0

#     result_array = []

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result_array.append(left[i])
#             i+=1
#         else:
#             result_array.append(right[j])
#             j+=1
        
#         result_array.extend(left[i:])
#         result_array.extend(right[j:])
    
#     return result_array

