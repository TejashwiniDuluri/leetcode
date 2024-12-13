# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return str(None)
        
        result_string = ""        
        left_str = self.serialize(root.left,)
        right_str =  self.serialize(root.right)

        result_string = str(root.val) + "," + left_str + "," + right_str
        print(result_string)
        return result_string


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        li = data.split(",")
        
        return self.preorder(li)


    def preorder(self, li):        
        if not li:
            return None

        val = li.pop(0)
        if val == 'None':
            return None
        else:
            root = TreeNode(val)

        root.left = self.preorder(li)
        root.right = self.preorder(li)
        return root



        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
node = tree.right
node.left = TreeNode(4)
node.right = TreeNode(5)

obj = Codec()
print(obj.serialize(tree))
print(obj.deserialize(obj.serialize(tree)))


