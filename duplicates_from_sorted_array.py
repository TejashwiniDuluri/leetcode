
nums = [1, 1, 2]
# nums = [1, 1, 1, 2, 2, 3]


# def remove_duplicates(nums):

#     temp = 1
#     duplicates = 0
#     for i in range(1, len(nums)):
#         print(i, temp, nums)
#         # if prev element and curr matches, swap with temp
#         if nums[i] != nums[i-1]:
#             nums[temp] = nums[i]
#             temp = temp+1
#         else:
#             duplicates = duplicates+1
#     return nums, len(nums) - duplicates


def remove_duplicates(nums):
    # d_index = 1

    # for s_index in range(0, len(nums) - 1):

    #     if nums[s_index] != nums[s_index + 1]:
    #         nums[d_index] = nums[s_index + 1]
    #         d_index += 1

    # return d_index

    # ===================================================

    nums[:] = sorted(set(nums))
    return len(nums)

    # ===================================================


# print(remove_duplicates(nums))


nums = [1, 1, 1, 2, 2, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]


def remove_duplicates(nums):
    count = 1
    j = 1
    uniques_elements = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count = count+1
        else:
            count = 1

        if count <= 2:
            nums[j] = nums[i]
            j = j+1
            uniques_elements = uniques_elements+1
    return nums, uniques_elements


print(remove_duplicates(nums))
