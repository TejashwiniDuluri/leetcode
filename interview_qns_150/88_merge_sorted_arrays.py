class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m-1 #2
        j = n-1 # 2
        k = m+n-1 #5

        while (i>=0 and j>=0):

            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j-=1
                
            else:
                nums1[k] = nums1[i]
                i-=1
            
            k-=1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

        return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# 1 => [1, 2,3, 0,0,6]
# 2 => [1, 2, 3, 0, 5, 6]
# 3 => [1, 2, 3, 3,5,6]
# 4 => [1,2,2,3,5,6]
# 5 => 

obj = Solution()
print(obj.merge(nums1, 3, nums2, 3))
