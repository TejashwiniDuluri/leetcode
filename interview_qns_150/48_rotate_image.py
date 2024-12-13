from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #transpose the matrix and then reverse the rows
        le = len(matrix)
        for i in range(le):
            for j in range(i+1, le):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for li in matrix:
            i = 0
            j = len(li)-1
            while i<j:
                li[i],li[j] = li[j], li[i]
                i+=1
                j-=1
            return matrix

        

obj=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(obj.rotate(matrix))




