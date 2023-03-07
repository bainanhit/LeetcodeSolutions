# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # DFS
    def compare(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A and B:
            return False
        # 判断当前节点及左右子树是否相等
        return A.val == B.val and self.compare(A.left, B.left) and self.compare(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False
        # 判断B是否是A，A左子树，A右子树的子结构
        return self.compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)