def guess(n):
    if n == 6:
        return 0
    elif n > 6:
        return -1
    else:
        return 1


def guessNumber(n):
    low = 0
    high = n

    while low <= high:
        mid = (low + high)//2
        print(low, high, mid)
        result = guess(mid)
        if result == 0:
            return mid
        elif result == -1:
            high = mid-1
        else:
            low = mid+1
    return -1


print(guessNumber(10))
