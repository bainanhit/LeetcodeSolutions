class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心
        cover = 0
        n = len(nums)
        if n == 1:
            return True
        cnt = 0
        # python不支持动态修改for循环中变量,使用while循环代替
        while cnt <= cover:
            cover = max(cover, nums[cnt]+cnt)
            # 判断
            if cover >= n-1:
                return True
            cnt += 1
        
        return False
            
            
            
# fu: lc 45.跳跃游戏2
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心
        n = len(nums)
        if n == 1:
            return 0
        end, max_pos = 0, 0
        step = 0
        for i in range(0, n-1):
            # 找跳最远的
            max_pos = max(max_pos, nums[i]+i)
            if i == end:
                # 遇到边界，就更新边界，并且步数加一
                end = max_pos
                step += 1
        
        return step

        