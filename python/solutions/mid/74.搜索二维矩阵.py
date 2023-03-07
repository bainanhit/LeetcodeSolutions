class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n-1
        while i < m and j >= 0:
            tmp = matrix[i][j]
            if tmp == target:
                return True
            elif tmp < target:
                i += 1
            else:
                j -= 1
        
        return False
                