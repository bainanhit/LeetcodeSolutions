# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 法一  dfs  暴力
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # rootSum(p,val) 表示以节点p为起点向下且满足路径总和为val的路径数目
        # O(N2) Z(N)
        self.res = 0

        def dfs(root, targetSum):
            if not root:
                return
            
            if root.val == targetSum:
                self.res += 1
            
            dfs(root.left, targetSum-root.val)
            dfs(root.right, targetSum-root.val)
        
        if not root:
            return 0
        dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.res
    


    # 法二： 前缀和
    # O(N) Z(N)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        presum = collections.defaultdict(int)
        presum[0] = 1
        
        def dfs(root, cur):
            if not root:
                return 0
            res = 0
            cur += root.val
            res += presum[cur-targetSum]
            # 记录前缀和个数
            presum[cur] += 1
            res += dfs(root.left, cur)
            res += dfs(root.right, cur)
            # 遍历完当前节点和其所以子节点之后，当前节点的前缀和就没有用了，就需要把map里的记录删除
            presum[cur] -= 1

            return res
        
        return dfs(root, 0)
