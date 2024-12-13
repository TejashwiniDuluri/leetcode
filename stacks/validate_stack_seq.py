class Solution:
    def validateStackSequences(self, pushed, popped):

        stack = []
        pop_index = 0
        for i in pushed:
            stack.append(i)
            if stack[-1] != popped[pop_index]:
                continue
            while (stack and stack[-1] == popped[pop_index]):
                stack.pop()
                pop_index += 1
        if stack:
            return False
        else:
            return True
        # print(stack)


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]

# pushed = [1]
# popped = [1]

pushed = [2, 1, 0]
popped = [1, 2, 0]

obj = Solution()
print(obj.validateStackSequences(pushed, popped))
