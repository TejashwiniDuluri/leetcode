
nums = [1, 2, 3, 1]
k = 3
nums = [1, 1]
k = 1
# nums = [99, 99]
# k = 2
nums = [1, 0, 1, 1]
k = 1
# nums = [1, 2, 3, 1, 2, 3]
# k = 2

# nums = [1, 2, 1]
# k = 0


def contains_duplicates(nums):

    obj = {}
    for i in range(len(nums)):
        if nums[i] in obj and i - obj[nums[i]] <= k:
            return True
        else:
            obj[nums[i]] = i
    return False


print(contains_duplicates(nums))
