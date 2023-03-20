# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历 递归
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_cur = float('-inf')

        def dfs(root):
            nonlocal max_cur
            
            if not root:
                return True
            is_left = dfs(root.left)
            # 中序遍历，验证是否从小到大
            if root.val > max_cur:
                max_cur = root.val
            else:
                return False
            is_right = dfs(root.right)
        
            return is_left and is_right
        
        return dfs(root)
    
    # 迭代法 中序遍历
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     stack = []
    #     cur = root
    #     pre = None
    #     while cur or stack:
    #         if cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         else:
    #             cur = stack.pop()
    #             if pre and cur.val <= pre.val:
    #                 return False
    #             pre = cur
    #             cur = cur.right
    #     return True

            
                
        
        
        