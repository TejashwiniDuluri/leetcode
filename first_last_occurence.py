
def find_first_element(n, target):
    low = 0
    length = len(n)
    high = length-1

    while low <= high and length > 0:
        mid = (low + high) // 2
        print(mid, low, high)
        if n[mid] == target and (mid == 0 or n[mid-1] != target):
            # mid matches but before element does not exists or does not match
            return mid
        elif n[mid] == target and n[mid-1] == target:
            # mid matches and before matches
            high = mid - 1

        elif n[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


def find_last_element(n, target):
    low = 0
    length = len(n)
    high = length-1

    while low <= high and length > 0:
        mid = (low + high) // 2
        if n[mid] == target and (mid == length-1 or n[mid+1] != target):
            # mid matches but next element does not exists or does not match
            return mid
        elif n[mid] == target and n[mid+1] == target:
            # mid matches and next matches
            low = mid + 1

        elif n[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


# ===========


def searchRange(nums, target):
    first = find_first_element(nums, target)
    last = find_last_element(nums, target)
    return [first, last]


print(searchRange([2, 2], 3))
