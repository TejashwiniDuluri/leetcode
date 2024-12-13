class Solution:
    def reverse(self, x: int) -> int:
        
        
        if x < 0: 
            st = -int(str(x)[::-1].replace("-", ""))
        else:
            st = int(str(x)[::-1])
        
        if st.bit_length() >= 32:
            return 0
        
        print(st.bit_length())
        

        return st
    
x = 120
x = 123
x = -123
x = 1534236469
x=1563847412
obj = Solution()
print(obj.reverse(x))
