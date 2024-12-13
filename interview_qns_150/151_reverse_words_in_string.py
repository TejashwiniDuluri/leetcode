class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.strip().split(" ")[::-1])
        
        #or 

        # two pointers approach
        
        s = s.split(" ")
        right = len(s)-1
        left = 0

        while left <= right-1:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return " ".join(s)

                



        

s = "the sky is blue"
obj  = Solution()
print(obj.reverseWords(s))