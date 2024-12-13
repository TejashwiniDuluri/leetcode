

def four_sum(nums, target):
    nums.sort()
    results = set()
    for i in range(0, len(nums) - 3):
        for j in range(i+1, len(nums) - 2):
            l = j + 1
            r = len(nums)-1
            while (l < r):
                # print(nums[i], nums[j], nums[l], nums[r])
                sum = nums[i] + nums[j]+nums[l] + nums[r]
                if sum == target:
                    results.add((nums[i], nums[j], nums[l], nums[r]))
                if sum > target:
                    r = r-1
                else:
                    l = l+1

    return list(results)


nums = [1, 0, -1, 0, -2, 2]
target = 0
# nums = [2, 2, 2, 2, 2]
# target = 8
print(four_sum(nums, target))
