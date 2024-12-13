class Solution:
    
    def increment(self, st):        
        value = 0
        for i in st:
            value += int(i)
        return str(value)

    def getLucky(self, s: str, k: int) -> int:        
        
        st = ""
        for i in s:
            st += str(ord(i) - 96)
        
        for i in range(k):            
            st = self.increment(st)
        
        return int(st)
        
obj= Solution()

s = "zbax"
k = 2

print(obj.getLucky(s, k))
            
            
        
    
    


        

        


