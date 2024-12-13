from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        columns= defaultdict(int)

        for ind, column in enumerate(list(zip(*grid))):
            columns[column] += 1        

        count = 0
        for i in grid:
            tup = tuple(i)
            if tup in columns:
                count += columns[tup]
                
                

        return count
        
obj = Solution()
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid =[[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

# grid = [[3,2,1],[1,7,6],[2,7,7]]
print(obj.equalPairs(grid))

