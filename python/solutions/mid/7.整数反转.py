class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x = str(x)
        res = ''
        if x[0] == '-':
            res += '-'
            x = x[1:]
        res += x[::-1]
        res = int(res)
        if -2**31 < res < 2**31-1:
            return res
        return 0


    # 法二
    def reverse(self, x: int) -> int:
        n = 0
        flag = False
        if x == 0:
            return 0
        if x < 0:
            flag = True
            x = -x
        while x:
            n = n*10 + x%10
            x = x//10
        
        if flag:
            n = -n

        if n <= -pow(2, 31) or n >= pow(2, 31) - 1:
            return 0
        return n