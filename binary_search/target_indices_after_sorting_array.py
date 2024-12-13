from typing import List
class Solution:

    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lenth = len(nums)
        left = 0
        right = lenth-1

        indices = []

        while right > left:
            mid = (left + right) //2   
            
            if nums[mid] == target:
                indices.append(mid)
                i = mid - 1
                j = mid+1  
                            
                while nums[i] == target and i>= 0:
                    indices.insert(0,i)
                    i-=1
                while j<= lenth-1 and nums[j] == target :
                    indices.append(j)
                    j+=1
                break
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid
            
        if left == right and target == nums[left]:
            indices.append(left)
        
        return indices
    

nums = [1,2,5,2,3]
target = 2

nums = [1,2,5,2,3]
target = 5

nums = [1]
target = 1

nums =[100,1,100]
target = 100

obj = Solution()
print(obj.targetIndices(nums, target))


        
