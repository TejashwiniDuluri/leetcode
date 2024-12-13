# import time
# import numpy as np

# # List
# list1 = list(range(1000000))
# list2 = list(range(1000000))

# start = time.time()
# result_list = [a + b for a, b in zip(list1, list2)]
# end = time.time()
# print(f"List addition time: {end - start}")

# # NumPy Array
# arr1 = np.array(list1)
# arr2 = np.array(list2)

# start = time.time()
# result_arr = arr1 + arr2
# end = time.time()
# print(f"NumPy addition time: {end - start}")

# a = np.array([[1,2,3], [1,2,3], [1,2,3]])
# b = np.array([[1,2,3], [1,2,3], [1,2,3]])
# print(a + b)

# matrix_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix_np[:,1])
# print(matrix_np[:,2])
# print(matrix_np[1,2])


s = {1, 2, 3}
item = s.pop()
print(item)
