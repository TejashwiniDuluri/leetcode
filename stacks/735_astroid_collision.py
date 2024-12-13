class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for i in asteroids:

            if not stack or i > 0:
                stack.append(i)
            
            else:
                while stack and stack[-1] > 0:

                    if stack[-1] == abs(i):
                        stack.pop()
                        break
                    if  stack[-1] < abs(i):
                        stack.pop()

                    else:
                        break
                else:
                    stack.append(i)
                    
        return stack

        # =======================================================================================================


asteroids = [5, 10, -5]
# asteroids = [8, -8]
# asteroids = [10, 2, -5]
# asteroids = [-2, -1, 1, 2]
# asteroids = [-2, 1, -2, -2]
# asteroids = [-2, 2, 1, -2]

obj = Solution()
print(obj.asteroidCollision(asteroids))
