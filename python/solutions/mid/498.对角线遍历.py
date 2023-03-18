class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 模拟，共有m+n-1条对角线
        m, n = len(mat), len(mat[0])
        size = m * n 
        res = []
        cnt = 0
        up = True # 向上flag
        i, j = 0, 0
        while cnt < size:
            res.append(mat[i][j])
            cnt += 1
            # 向右上方走
            if up:
                # 边界判断
                if j == n-1: # 到右边界，下移
                    i += 1         
                    up = not up
                elif i == 0: # 上边界，右移
                    j += 1
                    up = not up
                else: # 右上移动
                    i -= 1
                    j += 1
            # 左下走
            else:
                if i == m-1: # 到下边界，右移
                    j += 1
                    up = not up
                elif j == 0: # 到左边界，下移
                    i += 1
                    up = not up
                else:
                    i += 1
                    j -= 1
        return res