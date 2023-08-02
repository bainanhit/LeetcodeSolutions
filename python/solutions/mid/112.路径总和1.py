# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, targetSum)
        
    def dfs(self, root, _sum):
        if not root:
            return False
        # 到达叶子结点
        if not root.left and not root.right:
            if _sum == root.val:
                return True
            else:
                return False
        return self.dfs(root.left, _sum-root.val) or self.dfs(root.right, _sum-root.val)
        
         
# 迭代  
class solution:
    def haspathsum(self, root: TreeNode, targetsum: int) -> bool:
        if not root: 
            return False

        stack = []  # [(当前节点，路径数值), ...]
        stack.append((root, root.val))

        while stack: 
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetsum: 
                return True

            if cur_node.right: 
                stack.append((cur_node.right, path_sum + cur_node.right.val))    

            if cur_node.left: 
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False    
        
        

        
        