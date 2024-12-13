from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hash method
        d = OrderedDict()
        for index, val in enumerate(s):
            key = d.get(val)

            if key == None:
                d[val] = [index, 1]
            else:
                d[val] = [d[val][0], d[val][1]+1]

        for i in d:
            if d[i][1] == 1:
                return d[i][0]

        return -1
        # ====================


obj = Solution()
s = "leetcode"
s = "loveleetcode"
# s = "aadadaad"
print(obj.firstUniqChar(s))
