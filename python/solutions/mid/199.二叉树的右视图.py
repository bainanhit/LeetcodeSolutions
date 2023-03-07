# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        # queue = [root]
        queue = collections.deque()
        queue.append(root)
        # res.append(root.val)
        while queue:    
            s = len(queue)
            for i in range(s):
                node = queue.popleft()    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)
        return res
        
        