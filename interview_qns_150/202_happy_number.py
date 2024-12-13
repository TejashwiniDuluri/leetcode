class Solution:
    
    def isHappy(self, n: int) -> bool:

        hash_map = {}
        n = str(n)        
        while True:
            cur_res = 0
            for i in str(n):
                cur_res += int(i)**2            
            if cur_res in hash_map:
                return False
            else:
                hash_map[cur_res] = cur_res
                n = str(cur_res)
                
                if n == str(1):
                    return True
        
        


n = 19
n=2
# n = 7
obj = Solution()
print(obj.isHappy(n))