
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    
    def bfs(self, root):

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

    def pathInZigZagTree(self, label: int) :                
        root = TreeNode(1) 
        final_path = deque([])  
            
        def build_tree(root, val, level, label):
            
            dq = deque([root])

            while dq:
                
                dq_len = len(dq)
                
                level_dq = deque([])
                
                while dq_len > 0:
                    if val > label:
                        return

                    if level % 2 != 0:                        
                        node = dq.pop()     
                        node.right = TreeNode(val)
                        val += 1
                        node.left = TreeNode(val)                    
                        val += 1
                        level_dq.appendleft(node.right)
                        level_dq.appendleft(node.left)
                        
                    else:
                        node = dq.popleft()
                        node.left = TreeNode(val)                    
                        val += 1
                        node.right = TreeNode(val)
                        val += 1    
                        level_dq.append(node.left)               
                        level_dq.append(node.right)               

                    dq_len -= 1   
                                
                dq.extend(level_dq)
                
                level += 1
                if val > label:
                    return


        def label_path(root, path):
            nonlocal final_path

            path = path.copy()
            
            if root.val == label:   
            
                path.append(root.val)

                final_path = path
                return 
            
            path.append(root.val)
            
            if root.left:
                label_path(root.left, path)
            
            if root.right:
                label_path(root.right, path)

            return root

        build_tree(root, 2, 1, label)
        print(self.bfs(root))
        label_path(root, deque([]))
        return final_path

# obj =Solution()
# obj.pathInZigZagTree(label=16)

# class Solution:
#     def pathInZigZagTree(self, label: int) :

#         input_array = [[1]]

#         val = 2
#         level = 2
#         level_count = 1
        
#         while True:
        
#             level_values = deque([])
        
#             if level %2 == 0: 
#                 for i in range(level_count*2):
#                     level_values.appendleft(val)
#                     val+=1
#                     if i == label:
#                         return input_array
#             else:
#                 for i in range(level_count*2):
#                     level_values.append(val)
#                     val+=1
#                     if i == label:
#                         return input_array
            
#             level_count  = level_count * 2
#             level += 1
            
#             input_array.append(level_values)
        
# obj = Solution()
# print(obj.pathInZigZagTree(14))
