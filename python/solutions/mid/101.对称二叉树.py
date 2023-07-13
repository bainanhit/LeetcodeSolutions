# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归
        # O(N) Z(N)
        if not root:
            return True
        
        def cmp(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            return cmp(node1.left, node2.right) and cmp(node1.right, node2.left)
        
        return cmp(root.left, root.right)
        
            