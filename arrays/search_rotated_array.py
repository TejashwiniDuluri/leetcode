

def search_in_rotated_array(nums, target):
    mid = len(nums)//2
    low = 0
    high = len(nums)-1

    if nums[mid] == target:
        return nums[mid], mid

    while (low <= high):
        mid = (low+high)//2
        if nums[mid] == target:
            return nums[mid], mid

        if (nums[low] <= nums[mid]):
            if target <= nums[mid] and nums[low] <= target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target >= nums[mid] and target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
    return -1


nums = [5, 6, 0, 1, 2, 3, 4]
target = 0
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 2
# nums = [5, 1, 3]
# target = 3

print(search_in_rotated_array(nums, target))
