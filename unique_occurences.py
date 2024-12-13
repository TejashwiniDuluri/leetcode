
arr = [1, 2, 2, 1, 1, 3]


def find_unique_occurences(arr):
    counts = {}
    for i in arr:
        if counts.get(i):
            counts[i] += 1
        else:
            counts[i] = 1
    counts_altogether = list(counts.values())
    if len(counts_altogether) == len(list(set(counts_altogether))):
        return True
    else:
        return False


print(find_unique_occurences(arr))
