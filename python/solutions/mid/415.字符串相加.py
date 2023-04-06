class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 大数相加
        res = ''
        carry = 0
        i, j = len(num1)-1, len(num2)-1
        while i >= 0 or j>=0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res += str(tmp%10)
            i -= 1
            j -= 1

        if carry > 0:
            res += '1'
        
        return res[::-1]

# follow up
# 有负数进行加减： 分4种情况

