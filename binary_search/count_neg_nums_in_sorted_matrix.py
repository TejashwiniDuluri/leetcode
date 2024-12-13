from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])

        row = m -1
        col = 0
        count = 0

        while row >=0 and col < n:

            if grid[row][col] < 0:
                count += n - col
                row -=1
            else:
                col +=1
        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
obj = Solution()
print(obj.countNegatives(grid))