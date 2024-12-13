

def merge_sort(left, right):
    i = 0
    j = 0
    result_array = []
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


def findMedianSortedArrays(nums1, nums2):
    result_array = merge_sort(nums1, nums2)
    mid = len(result_array)//2
    if len(result_array) % 2 == 0:
        return (result_array[mid]+result_array[mid-1])/2
    else:
        return result_array[mid]


findMedianSortedArrays([1, 3], [2])
