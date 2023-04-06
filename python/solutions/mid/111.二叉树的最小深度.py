# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:  
        # 递归
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left and root.right:
            return 1 + right
        if not root.right and root.left:
            return 1 + left
        return 1 + min(left, right)

        # 迭代
        # 层序遍历，遇到第一个左右子树都为空的即为最小深度

    # fu: 二叉树最大深度
    # 递归
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)  # 左
        right = self.maxDepth(root.right) # 右
        return 1 + max(left, right) # 中