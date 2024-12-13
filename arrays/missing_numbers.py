

def merge(left, right):

    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def missing_number(nums):
    n = len(nums)
    # nums = merge_sort(nums)
    nums.sort()
    if n != nums[-1]:
        return n
    for index, value in enumerate(nums):
        if index != value:
            return index


print(missing_number([3, 0, 1]))
