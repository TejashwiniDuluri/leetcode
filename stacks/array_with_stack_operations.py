class Solution:
    def buildArray(self, target, n):
        result = []
        current = 1
        for i in target:
            # if current == i:
            #     result.append("Push")
            #     current += 1

            # elif i > current:
            #     while current < i:
            #         result.extend(["Push", "Pop"])
            #         current += 1
            #     if i == current:
            #         result.append("Push")
            #         current += 1

            while i != current:
                result.extend(["Push", "Pop"])
                current += 1

            if i == current:
                result.append("Push")
                current += 1

        return result


target = [1, 3]
n = 3
# target = [1, 2, 3]
# n = 3
# target = [1, 2]
# n = 4
# target = [2, 3, 4]
# n = 4
obj = Solution()
print(obj.buildArray(target, n))
