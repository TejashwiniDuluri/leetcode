from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # 4 loops
        # 1 => for traversing left to right
        # 2 => for traversing top to bottom
        # 3 => for traversing right to left
        # 4 => for traversing bottom to top

        row_start = 0
        row_end = len(matrix)-1
        col_start = 0
        col_end = len(matrix[0])-1

        result = []

        while row_start <= row_end and col_start <= col_end:
            

            # 1 => for traversing left to right
            for i in range(col_start, col_end+1):                
                result.append(matrix[row_start][i])
            row_start += 1

            
            # 2 => for traversing top to bottom
            for i in range(row_start, row_end+1):                
                result.append(matrix[i][col_end])
            col_end-=1
            
            if row_start<= row_end:
                # 3 => for traversing right to left            
                for i in range(col_end, col_start-1, -1):                
                    result.append(matrix[row_end][i])
                row_end-=1

            if col_start <= col_end:
                # 4 => for traversing bottom to top
                for i in range(row_end, row_start-1, -1):
                    result.append(matrix[i][col_start])
                col_start+=1


        return result

obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix =[[2,5],[8,4],[0,-1]]
matrix =[[7],[9],[6]]
print(obj.spiralOrder(matrix))