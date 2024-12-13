class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        index = 0
        traverse = 1 # 1=> going down -1 => going up
        
        rows = [''] * numRows
        print(rows)
        for i in s:
            rows[index] += i
            if index == numRows - 1:
                traverse = -1 
            elif index == 0:
                traverse = 1 # going down

            index += traverse
            print(rows)
                
        return "".join(rows)
        
obj = Solution()
s = "PAYPALISHIRING"
numRows = 3
# s = "ABC"
# numRows = 1
print(obj.convert(s, numRows))
        