
nums = [4, 1, 2, 1, 2]
obj = {}


def find_single_num(nums):
    for i in nums:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    for i in obj:
        if obj[i] == 1:
            return i
