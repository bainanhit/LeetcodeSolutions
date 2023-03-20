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