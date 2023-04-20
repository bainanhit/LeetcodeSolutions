class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        num1_lst = list(num1)
        num2_lst = list(num2)
        res = [0] * (len(num1_lst)+len(num2_lst))
        # 逆序遍历
        for i in range(len(num1_lst)-1, -1, -1):
            for j in range(len(num2_lst)-1, -1, -1):
                tmp = int(num1_lst[i]) * int(num2_lst[j])
                # 个位
                idx = i+j+1
                # 十位
                idx2 = i+j
                # 先相加 再进位
                tmp += res[idx]
                res[idx] = tmp % 10
                res[idx2] += tmp // 10
                
        if res[0] == 0:
            res = res[1:]
        return ''.join(str(ch) for ch in res)
