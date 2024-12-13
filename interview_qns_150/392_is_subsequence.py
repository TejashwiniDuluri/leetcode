class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        
        s_ind = 0
        s_len = len(s)

        for val in t:
            if s_ind >= s_len:
                break
            if val == s[s_ind]:
                s_ind+=1
        if s_len == s_ind:
            return True
        return False



s = "abc"
t = "ahbgdc"  
s = "axc"
t = "ahbgdc" 
s = ""
t = "ahbgdc"     
obj = Solution()
print(obj.isSubsequence(s,t))