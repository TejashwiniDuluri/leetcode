# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
    
    
        
    def trimBST(self, root, low, high) :
        if not root:
            return None
        
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
        
    
    
    def levelOrder(self, root) :        
        results = []
        
        if not root:
            return results
        
        
        queue = []
        queue.append(root)
        
        while queue:
            
            queue_len = len(queue)
            curr_level_list = []
            
            while queue_len > 0:
                node = queue.pop(0)
                curr_level_list.append(node.val)
                queue_len -= 1
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            results.append(curr_level_list)
        return results
        
obj = Solution()
# case 1
# obj.insert(1)          
# obj.insert(0)          
# obj.insert(2)

#case 2
# obj.insert(3)          
# obj.insert(0)          
# obj.insert(4)
# obj.insert(2)
# obj.insert(1)

#case 3
# obj.insert(3)          
# obj.insert(1)          
# obj.insert(4)
# obj.insert(2)

#case 4
obj.insert(3)          
obj.insert(2)          
obj.insert(1)
obj.insert(4)


# print(obj.levelOrder(obj.trimBST(obj.root, 1, 2)))
# print(obj.levelOrder(obj.trimBST(obj.root, 1, 3)))
# print(obj.levelOrder(obj.trimBST(obj.root, 3, 4)))
print(obj.levelOrder(obj.trimBST(obj.root, 1, 1)))

          

    
    
                
        