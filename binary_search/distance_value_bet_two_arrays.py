from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:        
        
        arr2.sort()
        length = len(arr2)

        count = 0
        for i in arr1:  
            
            left = 0
            right = length-1
            isMatch=False

            while left<=right :                               
                mid = (left + right) //2            

                if abs(i - arr2[mid]) <= d:                
                    isMatch=True
                    break
                else:                    
                    right = mid-1

            if not isMatch:
                count+=1
            

        return count

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2

obj = Solution()
print(obj.findTheDistanceValue(arr1, arr2, d))
        
[4, 5, 8]
[1, 8, 9, 10]