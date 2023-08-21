def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        presum = collections.defaultdict(int)
        presum[0] = 1
        
        def dfs(root, cur):
            if not root:
                return 0
            res = 0
            cur += root.val
            res += presum[cur-targetSum]
            presum[cur] += 1
            res += dfs(root.left, cur)
            res += dfs(root.right, cur)
            # 遍历完当前节点和其所以子节点之后，当前节点的前缀和就没有用了，就需要把map里的记录删除
            presum[cur] -= 1

            return res
        
        return dfs(root, 0)