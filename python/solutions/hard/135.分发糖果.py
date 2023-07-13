class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 两次遍历，从前往后+从后往前
        n = len(ratings)
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(n-2, -1, -1):
            # 保证第i个小孩的糖果数量既大于左边的也大于右边的
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i+1] + 1, candy[i])
        
        return sum(candy)

    # fu: 围城一个环
    # 在首尾补充两个元素，首部补充原尾部元素，尾部补充原首部元素，
    # 计算方法还是一样的，只是最后求和的时候刨去添加的首尾。