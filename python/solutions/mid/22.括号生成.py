class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # 回溯
        def backtrack(in_idx: int, out_idx: int, tmp_res: str):
            # 边界条件
            if in_idx > n or out_idx > n:
                return 
            if len(tmp_res) == 2*n:
                res.append(tmp_res)
                return

            # 递归处理，拼接左括号 右括号，先递归左括号才满足有效性
            if n - in_idx:
                backtrack(in_idx+1, out_idx, tmp_res+'(')
            if in_idx - out_idx:
                backtrack(in_idx, out_idx+1, tmp_res+')')
        
        backtrack(0, 0, '')
        return res
            