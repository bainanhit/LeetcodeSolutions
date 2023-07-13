class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 逆推 剩余元素在原始数据中的位置
        if n<1 or m<1:
            return -1
        last = 0
        # i代表人数
        for i in range(2, n+1):
            last = (last+m) % i
        
        return last