# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = 0
        que = []
        res = []
        if not root:
            return res

        que.append(root)
        while que:
            n = len(que)
            
            tmp = []
            for i in range(n):
                node = que.pop(0)
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if flag % 2 == 1:
                tmp.reverse()
            res.append(tmp)
            flag += 1
        
        return res

