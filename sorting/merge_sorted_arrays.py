
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


nums1 = [1]
m = 1
nums2 = []
n = 0

nums1 = [0]
m = 0
nums2 = [1]
n = 1

nums1 = [7, 8, 9, 0, 0, 0, 0, 0]
m = 3
nums2 = [1, 2, 3, 4, 5]
n = 5
# reference
# https://afteracademy.com/blog/merge-two-sorted-arrays/


def merge(nums1, num2):
    i = m-1  # last valid element index of nums1. 0 are not valid here, they are to fill the gaps
    j = n-1  # last index of nums2
    k = m+n-1  # last index of nums1

    while i >= 0 and j >= 0:
        print(1)
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

    while (i >= 0):
        nums1[k] = nums1[i]
        i = i-1
        k = k-1
    while (j >= 0):
        nums1[k] = nums2[j]
        j = j-1
        k = k-1

    return nums1


# def merge(nums1, nums2) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     i = m - 1
#     j = n - 1
#     k = m + n - 1
#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
#     return nums1


print(merge(nums1, nums2))
