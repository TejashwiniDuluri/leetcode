class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_elements = path.split("/")

        for i in path_elements:
            if not stack and i == "..":
                continue
            if i == "..":
                stack.pop()
            elif i == "." or i == "":
                continue

            else:
                stack.append(i)
            print(stack)

        return "/"+"/".join(stack)


path = "/a//b////c/d//././/.."
path = "/a/../../b/../c//.//"
path = "/a/./b/../../c/"
path = "/home//foo/"
path = "/../"
path = "/a//b/c/"
path = "/home/"
obj = Solution()
print(obj.simplifyPath(path))
