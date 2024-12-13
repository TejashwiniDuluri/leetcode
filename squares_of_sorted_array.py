

def divide(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    left = divide(nums[:mid])
    right = divide(nums[mid:])
    return merge_sort(left, right)


def merge_sort(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    result += left[i:]
    result += right[j:]
    return result


def sort_squared_array(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return divide(nums)


nums = [-4, -1, 0, 3, 10]
print(sort_squared_array(nums))
