# nums = [2, 7, 11, 15]
# target = 9
nums = [3, 2, 4]
target = 6


def two_sum(nums):
    obj = {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if diff in obj:
            return [obj[diff], i]
        else:
            obj[nums[i]] = i
    return []


print(two_sum(nums))
