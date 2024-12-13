
# nums = [1, 2, 3, 4, 5, 6, 7]
k = 5
nums = [1, 2]


def get_k(length, k):
    while (k > length):
        return k-length
    return k


def rotate_array(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[0:-k]
    return nums


# print(rotate_array(nums, k))


# def reverse(array, start, end):
#     print(array, start, end)
#     while (start < end):
#         temp = array[start]
#         array[start] = array[end]
#         array[end] = temp
#         start += 1
#         end -= 1
#     return array


# def rotate_array(nums, k):
#     k = k % len(nums)
#     reverse(nums, 0, len(nums)-1)
#     reverse(nums, 0, k-1)
#     reverse(nums, k, len(nums)-1)
#     return nums


print(rotate_array(nums, k))
