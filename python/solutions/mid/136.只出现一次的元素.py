class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 常数空间：位运算
        res = 0
        for num in nums:
            res ^= num
        
        return res
