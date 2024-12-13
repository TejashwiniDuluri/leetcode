
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinarySearchTree:
    
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, val):
        self.root = self._insert(self.root, val)
        
    def _insert(self, root, val):
        
        if not root :
            
            return TreeNode(val)
        
        elif val < root.val:
            root.left = self._insert(root.left, val)
        
        elif val > root.val:
            root.right = self._insert(root.right, val)
        
        return root
        
    def delete(self, val):
        self.root = self._delete(self.root, val)
    
    def _delete(self, root, val):            
        if not root:
            return root
        
        elif val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
                
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # replace matched node value with elected node and delete the target node
                # elected node => inorder successor => find min value from right of the node
                root.val = self.in_order_successor(root.right)
                self._delete(self.right, root.val)
        
        return root
    
    def in_order_successor(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr
            
    def inorder(self):
        # left, root, right
        result = []
        self._inorder(self.root, result)
        return result
        
        # result = []
        # if root:
        #     result += self.inorderTraversal(root.left)
        #     result.append(root.val)
        #     result += self.inorderTraversal(root.right)
        # return result 
    
    def _inorder(self, root, result):
        if not root:
            return root
        if root.left:
            self._inorder(root.left, result)
        result.append(root.val)
        if root.right:
            self._inorder(root.right, result)
                
    
    def preorder(self, root):
        # root, left, right
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, root, result):
        if not root:
            return root
        result.append(root.val)
        if root.left:
            self._preorder(root.left, result)
        if root.right:
            self._preorder(root.right, result)
          
    def postorder(self, root):
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, root, result):
        if not root:
            return root
        if root.left:
            self._postorder(root.left, result)
        if root.right:
            self._postorder(root.right, result)
        result.append(root.val)
        
    
obj = BinarySearchTree()
obj.insert(1)
obj.insert(2)
obj.insert(3)
print(obj.inorder())

