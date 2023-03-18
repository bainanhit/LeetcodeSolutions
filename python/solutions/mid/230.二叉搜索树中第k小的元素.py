# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历 栈 
        stack = []

        while root or stack:
            # 到左下角 最小节点
            if root:
                stack.append(root)
                root = root.left
            else:
                # 中序遍历  从小到大
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
        return 0



