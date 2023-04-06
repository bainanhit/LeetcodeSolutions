# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 层序遍历 设置判断标志
        stop = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            tmp_len = len(queue)
            for _ in range(tmp_len):
                node = queue.popleft()
                if node.left:
                    if stop:
                        return False
                    queue.append(node.left)
                else:
                    stop = 1
                if node.right:
                    if stop:
                        return False
                    queue.append(node.right)
                else:
                    stop = 1
        return True 