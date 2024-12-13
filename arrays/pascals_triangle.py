

# 1
# 1 1
# 1 2 1
# 1 3 3  1
# 1 4 6  4  1
# 1 5 10 10 5 1

# def get_rows(numRows):

#     result = []

#     for i in range(1, numRows+1):
#         row_list = [1]
#         if i == 1:
#             result.append(row_list)
#             continue

#         for j in range(1, len(result[i-2])):
#             row_list.append(result[i-2][j-1] + result[i-2][j])
#         row_list.append(1)
#         result.append(row_list)
#     return result


# def get_index_row(rowIndex):

#     result = []

#     for i in range(1, rowIndex+2):
#         row_list = [1]
#         if i == 1:
#             result = row_list
#             continue
#         for j in range(1, len(result)):
#             row_list.append(result[j-1] + result[j])
#         row_list.append(1)
#         result = row_list
#     return result

def generate_pascals_triangle(n):
    triangle = []

    for row in range(n):
        # Start each row with a "1"
        current_row = [1]

        # Calculate the inner values for the row, if it's not the first row
        if row > 0:
            for col in range(1, row):
                current_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])

            # End each row with a "1"
            current_row.append(1)

        triangle.append(current_row)

    return triangle


print(generate_pascals_triangle(3))
