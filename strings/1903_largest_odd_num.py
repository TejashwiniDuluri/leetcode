class Solution:
    def largestOddNumber(self, num: str) -> str:

        for i in range(len(num)-1, -1, -1):            
            if int(num[i])%2 != 0:
                return num[0:i+1]
        return ""

obj = Solution()
num = "52"
# num = "4206"
# num = "35427"
print(obj.largestOddNumber(num))



