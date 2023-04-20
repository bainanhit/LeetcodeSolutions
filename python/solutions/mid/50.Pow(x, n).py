class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂
        # 分奇偶 
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x, n = 1/x, -n
        
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n >>= 1
        
        return res
        