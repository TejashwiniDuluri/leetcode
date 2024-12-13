# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.root = root
#         self.inorder_tree_root = TreeNode(0)
#         self.curr_node = self.inorder_tree_root 
#         self.construct_inorder_tree(self.root)
#         self.pointer = self.inorder_tree_root

#     def next(self) -> int:        
#         #self.inorder(self.inorder_tree_root)
#         val = self.pointer.right.val
#         self.pointer = self.pointer.right
#         return val
        

#     def hasNext(self) -> bool:
#         return True if self.pointer.right else False


#     def construct_inorder_tree(self, root):
#         if root:
#             self.construct_inorder_tree(root.left)                             
#             new_inorder_node = TreeNode(root.val)
#             self.curr_node.right = new_inorder_node
#             self.curr_node = self.curr_node.right
#             self.construct_inorder_tree(root.right)     
#         return root 


#     def inorder(self, root):
#         if root:
#             self.inorder(root.left)
#             print(root.val)
#             self.inorder(root.right)
#         return root

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

######## optimized sol here #####

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.stack = []
        self.inorder(root)
        
    def next(self) -> int:        
        
        top = self.stack.pop()
        
        if top.right:
            self.inorder(top.right)
        
        return top.val
                

    def hasNext(self) -> bool:
        return True if self.stack else False


    def inorder(self, root):
        while root:
            self.stack.append(root)
            root= root.left
            
            
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()