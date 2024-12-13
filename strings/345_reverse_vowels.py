class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a" : 1, "e" : 1, "i" : 1, "o" : 1, "u" : 1, "A" : 1, "E" : 1, "I" : 1, "O" : 1,"U" : 1}

        left = 0
        right = len(s) - 1
        
        s = list(s)

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left +=1
                right -=1
            if s[left] not in vowels:
                left +=1
            if s[right] not in vowels:
                right -=1
            
        return "".join(s)
            
            


obj = Solution()
s = "IceCreAm"
print(obj.reverseVowels(s))