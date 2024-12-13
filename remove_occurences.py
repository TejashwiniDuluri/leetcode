
nums = [3, 2, 2, 3]
val = 3
# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
# nums = []
# val = 2


def find_occurences(nums, val):
    i = -1
    k = -1
    count = 0
    for i in range(len(nums)-1, -1, -1):
        # if nums[i] != val and nums[k] != val:
        #     nums[k] = "_"
        #     k = k-1
        if nums[i] == val and nums[k] != val:
            nums[i] = nums[k]
            nums[k] = "_"
            k = k-1
            count = count+1
        elif nums[i] == val and nums[k] == val:
            nums[k] = "_"
            k = k-1
            count = count+1

    return nums, len(nums) - count


print(find_occurences(nums, val))
