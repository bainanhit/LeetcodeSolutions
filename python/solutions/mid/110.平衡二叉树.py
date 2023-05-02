# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 递归
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right)+1

        if not root:
            return True
        if abs(dfs(root.left)-dfs(root.right)) > 1:
            return False
        # 左右子树高度差都小于等于1
        return self.isBalanced(root.left) and self.isBalanced(root.right)