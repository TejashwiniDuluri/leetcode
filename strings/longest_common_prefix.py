class Solution:
    def longestCommonPrefix(self, strs) -> str:
        #//////// first 
        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0
        prefix = ""
        min_length_string = min(len(first), len(last))

        while (i < min_length_string) and first[i] == last[i]:
            i+=1
            prefix += first[i]
        
        return prefix
    
        #//////// second

        min_len_string = min(strs, key=len)
        print(min_len_string)

        i = 0
        common_prefix = ""
        for char in min_len_string:
            for j in strs:
                print(char, j[i])
                if j[i] != char:
                    return common_prefix
            else:
                print(char, j[i], "===else ")
                common_prefix += char
            i+=1
        
        return common_prefix

obj = Solution()
strs = ["flower","flow","floight"]
strs = ["cir","car"]

print(obj.longestCommonPrefix(strs))





        