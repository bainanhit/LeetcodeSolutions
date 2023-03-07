# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue_node = []
        queue_val = []
        queue_node.append(root)
        queue_val.append(root.val)
        total = 0
        
        while queue_node:
            node = queue_node.pop()
            num = queue_val.pop()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    queue_node.append(left)
                    queue_val.append(left.val + num*10)
                if right:
                    queue_node.append(right)
                    queue_val.append(right.val + num*10)
        
        return total
            
    