
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
    
    
    def levelOrder(self, root) :        
        results = []
        
        if not root:
            return results
        
        queue = []
        queue.append(root)
        
        order = "left"
        
        while queue:
            
            queue_len = len(queue)
            curr_level_list = []
            
            while queue_len > 0:
                
                node = queue.pop(0)
                
                if order == "left":
                    curr_level_list.append(node.val)
                else:
                    curr_level_list.insert(0, node.val)
                    
                queue_len -= 1
                                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                                
            order = "right" if order == "left" else "left"
            results.append(curr_level_list)
        return results
    

obj = Solution()
obj.insert(3)
obj.insert(9)
obj.insert(20)
obj.insert(15)
obj.insert(7)

print(obj.levelOrder(obj.root))
                
                