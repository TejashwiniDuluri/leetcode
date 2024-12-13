class Solution:

    # def reverse_string(self,st, left, right):
        
    #     while left< right:
    #         st[left], st[right] = st[right], st[left]
    #         left +=1
    #         right -=1
    #     return st
        
    # def reverseWords(self, s: str) -> str:
    #     s = list(s)
    #     left = 0
    #     for index, char in enumerate(s):
    #         if char == " ":   
    #             print(index)                         
    #             s = self.reverse_string(s, left, index-1)
    #             left = index +1
    #     s = self.reverse_string(s, left, index)
    #     return ''.join(s)

    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])






s = "Let's take LeetCode contest"
obj  =Solution()
print(obj.reverseWords(s))
