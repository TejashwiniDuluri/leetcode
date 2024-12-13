from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #=>[temp, ind]
        res = [0] * len(temperatures)

        for  ind, i in enumerate(temperatures):
            
            while stack and i > stack[-1][0]:
                temp, temp_ind = stack.pop()
                res[temp_ind] = ind - temp_ind
            
            stack.append([i, ind])
        
        return res


            


obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(obj.dailyTemperatures(temperatures))
        