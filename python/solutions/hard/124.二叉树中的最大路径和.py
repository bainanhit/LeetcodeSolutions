# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    一颗三个节点的小树的结果只可能有如下6种情况：
        根 + 左 + 右
        根 + 左
        根 + 右
        根
        左
        右
    分析上述6种情况， 只有 2,3,4 可以向上累加，而1,5,6不可以累加
    然后使用递归，选择小树的最大路径和的情况，拼凑成一颗大树
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        
        def scan(root):
            if not root:
                return 0
            # 如果子树路径和为负则应当置0表示最大路径不包含子树 
            left = max(0, scan(root.left))
            right = max(0, scan(root.right))
            # 判断在该节点包含左右子树的路径和是否大于当前最大路径和
            self.res = max(self.res, left+right+root.val)
            # 选择左子树/右子树+当前节点
            return max(left, right) + root.val

        scan(root)
        return self.res

