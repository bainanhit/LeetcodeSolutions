class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # O(logn**2) Z(1)
        def count_(num):
            # 计算当前元素个数
            cnt = 0
            width = 1
            while True:
                if num + width -1 <= n:
                    # n 的值大于等于当前层的最大值, 说明当前层数的个数可以全部添加
                    cnt += width
                    num *= 10
                    width *= 10
                else:
                    # n 的值小于当前层的最大值则只能添加部分个数或者不添加, 并跳出循环
                    if n - num >= 0:
                        cnt += n - num + 1
                    break
            
            return cnt

        cnt = 0
        num = 1
        while True:
            # 要找到第 k 个元素, 需要经过 k - 1 个元素
            if cnt == k-1:
                break
            # 以 num 为根, 以 n 为最大值的十叉树的元素总个数
            tmp = count_(num)
            if cnt + tmp >= k:
                # 以 num 为根的十叉树内有第 k 个元素
                num *= 10
                cnt += 1
            else:
                num += 1
                cnt += tmp
        
        return num

                
            
            
            
            