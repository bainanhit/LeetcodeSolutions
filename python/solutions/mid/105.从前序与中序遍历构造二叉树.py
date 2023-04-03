# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root_val = preorder[0]
        inorder_root_idx = inorder.index(root_val)
        root = TreeNode(val=root_val)

        # 适用于左右子树没有重复元素的情况
        left = inorder[: inorder_root_idx]
        right = inorder[inorder_root_idx + 1:]

        # 递归遍历
        root.left = self.buildTree(preorder[1: 1+inorder_root_idx], left)
        root.right = self.buildTree(preorder[1+inorder_root_idx:], right)
        return root