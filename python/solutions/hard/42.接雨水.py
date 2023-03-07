class Solution:
    
    def trap(self, height: List[int]) -> int:
        # 双指针法
        n = len(height)
        if n <= 2:
            return 0
        max_left = height[0]
        max_right = height[n-1]
        res = 0
        left, right = 0, n-1
        while left <= right:
            if max_left < max_right:
                if height[left] < max_left:
                    res += max_left - height[left]
                max_left = max(max_left, height[left])
                left += 1
            else:
                if height[right] < max_right:
                    res += max_right - height[right]
                max_right = max(max_right, height[right])
                right -= 1
        
        return res
            
    
    def trap(self, height: List[int]) -> int:
        # 动态规划法
        n = len(height)
        if n <= 2:
            return 0
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        res = 0
        # 每个柱子左边最大高度
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        # 每个柱子右边最大高度
        max_right[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            max_right[j] = max(max_right[j+1], height[j])

        # 求和
        for k in range(1, n-1):
            cnt = min(max_left[k], max_right[k])-height[k]
            if cnt > 0:
                res += cnt
        
        return res
        




