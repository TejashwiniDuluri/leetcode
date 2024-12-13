from typing import List

class Solution:
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def compute(left, right, operator):
            results = []
            #left is a list and right is a list
            for l in left:
                for r in right:
                    if operator == "+":
                        results.append(l+r)
                    elif operator == "-":
                        results.append(l-r)
                    elif operator == "*":
                        results.append(l*r)
            
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, ch in enumerate(expression):
                
            if ch == "*" or ch == "+" or ch == "-":
                #evaluate left and right part
                left = self.diffWaysToCompute(expression[:index])
                # print(left, "==== left ====")
                right = self.diffWaysToCompute(expression[index+1 : ])
                # print(right, "==== right ====")

                results.extend(compute(left, right, ch))
        
        return results



obj = Solution()
expression = "2-1-1"
print(obj.diffWaysToCompute(expression))
        