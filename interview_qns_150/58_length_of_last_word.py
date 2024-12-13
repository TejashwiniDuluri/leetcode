class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # st = ""
        # s_length = len(s)-1

        # for index in range(s_length, -1,-1):
        #     if s[index] == " " and st == "":
        #         continue
        #     elif s[index] == " ":
        #         return len(st)
        #     else:
        #         st = s[index] + st
        # return len(st)

        return len(s.strip().split(" ")[-1])



obj = Solution()
s = "Hello World"
s = "   fly me   to   the moon  "
# s ="a"
print(obj.lengthOfLastWord(s))