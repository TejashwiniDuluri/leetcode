class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # j = len(needle)-1
        
        # start = 0
        
        # for index, i in enumerate(haystack):
        #     if index < j:
        #         continue                
        #     elif haystack[start:index+1] == needle:
        #         return start
        #     else:
        #         start +=1

        # return -1
        return haystack.find(needle)



haystack = "sadbutsad"
needle = "sad"
haystack = "leetcode"
needle = "leeto"
obj = Solution()
print(obj.strStr(haystack, needle))
        