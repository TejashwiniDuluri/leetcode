
class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        XOR Operation (^): This operation gives the sum of two bits without considering the carry.
        AND Operation (&): This operation, followed by a left shift, gives the carry.
        Here is the step-by-step algorithm:

        Step 1: Use the XOR operation to find the sum of a and b without carry.
        Step 2: Use the AND operation to find the carry, then left shift the carry by 1 bit.
        Step 3: Repeat the above steps until the carry becomes zero.
        """
        while (b != 0) : # b here is carry forwarded 1 value
            tmp = (a & b) << 1             
            a = a ^ b
            b = tmp

        return a

        

        
obj = Solution()
print(obj.getSum(2, 3))
print(obj.getSum(-1, 1))
