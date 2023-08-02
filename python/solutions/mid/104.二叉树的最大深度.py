# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归
        res = 0
        def dfs(root, level):
            nonlocal res
            if not root:
                return
            left = dfs(root.left, level+1)
            right = dfs(root.right, level+1)
            res = max(res, level)

        if not root:
            return 0
        dfs(root, 0)
        return res+1
    

# 法二：迭代
import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans