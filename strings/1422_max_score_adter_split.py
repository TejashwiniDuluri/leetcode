class Solution:
    def maxScore(self, s: str) -> int:
        max_ones = 0
        for i in s:
            if i == "1":
                max_ones +=1

        left_zeros = 0
        max_sum = 0

        for i in range(1, len(s)):            
            if s[i-1] == "0":
                left_zeros += 1             
            else:
                max_ones -= 1 
            
            max_sum = max(max_sum,left_zeros + max_ones)
        return max_sum
