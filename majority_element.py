
nums = [1, 1, 2, 2, 3, 4, 4,  4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
############################################################################################################
# sort method
nums = [2, 2, 1, 1, 1, 2, 2]
nums = [3, 3, 4]
# nums = [6, 5, 5]


def merge(left, right):

    i = 0
    j = 0
    result_array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_array.append(left[i])
            i = i+1
        else:
            result_array.append(right[j])
            j = j+1
    result_array += left[i:]
    result_array += right[j:]
    return result_array


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[0:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


# sorting technique
def find_majority_element(nums):
    nums = merge_sort(nums)
    print(nums)
    print(len(nums)/2)
    return nums[len(nums)//2]


# moores voting algo
def find_majority_element(nums):

    majority = 0
    votes = 0

    for i in nums:
        if votes == 0:
            majority = i
            votes = 1
        elif i == majority:
            votes += 1
        else:
            votes = votes - 1
    return majority


print(find_majority_element(nums))
