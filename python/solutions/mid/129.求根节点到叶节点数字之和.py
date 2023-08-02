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
            
            
    # 递归
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root, tmp_sum):
            nonlocal res
            if not root:
                return
            k = root.val + tmp_sum*10
            if not root.left and not root.right:
                res += k
            
            dfs(root.left, k)
            dfs(root.right, k)
        
        dfs(root, 0)
        return res
    