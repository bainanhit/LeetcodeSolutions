class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # res的值是在1~49范围内的均匀分布
        while True:
            res = (rand7()-1)*7 + (rand7())
            # 剔除大于40的值，1-40等概率出现
            if res <= 40:
                break
        
        return res%10+1