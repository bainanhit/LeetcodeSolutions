class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        if n <= 1:
            return 1
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
    
        for i in range(3, n+1):
            for j in range(0, n):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[n]
                
# fu: 返回不同的二叉搜索树
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def helper(left, right):
            res = []
            if left > right:
                res.append(None)
                return res
            # 产生的以当前i为根结点的BST（子）树有left_nodes.size() * right_nodes.size()个，遍历每种情况，即可生成以i为根节点的BST序列；
            # 然后以for循环使得[left, right]中每个结点都能生成子树序列。
            
            for i in range(left, right+1):
                leftnode = helper(left, i-1)
                rightnode = helper(i+1, right)
                
                for leftn in leftnode:
                    for rightn in rightnode:
                        node = TreeNode(i, leftn, rightn)
                        res.append(node)
            return res
        
        result = helper(1, n)
        return result