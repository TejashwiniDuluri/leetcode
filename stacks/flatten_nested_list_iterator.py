# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

class NestedInteger:
    def __init__(self, i):
        self.i = i

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        if type(self.i) == int:
            return True
        else:
            return False

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

        return self.i

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """

        result = []
        for elem in self.i:
            result.append(elem)
        return result


class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.flattend_list = []
        self.construct_flatten_list(nestedList)

    def construct_flatten_list(self, nested_list):

        for i in nested_list:
            if i.isInteger():
                self.flattend_list.append(i.getInteger())
            else:
                self.construct_flatten_list(i.getList())

    def next(self) -> int:
        print(self.flattend_list, "==")
        return self.flattend_list.pop(0)

    def hasNext(self) -> bool:
        try:
            if self.flattend_list[-1] != None:
                return True
            else:
                False
        except:
            return False


nestedList = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(
    2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
nestedList = [NestedInteger(0)]
# # Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
print(v)
