
digits = [1, 2, 3]

digits = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]


def plus_one(digits):
    inc_element = "".join([str(i) for i in digits])
    inc_element = int(inc_element)+1
    print(inc_element)
    return [int(i) for i in str(inc_element)]


print(plus_one(digits))
