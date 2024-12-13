

def selection_sort(array):

    n = len(array)

    for i in range(n):
        mini = i

        for j in range(i+1, n):
            if array[j] < array[mini]:
                mini = j

        array[mini], array[i] = array[i], array[mini]


    return array


a = [12, 12, 10, 9, 8]
print(selection_sort(a))
