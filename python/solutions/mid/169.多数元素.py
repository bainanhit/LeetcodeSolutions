class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 投票法
        # O(N)时间复杂度
        cnt = 1
        maj = nums[0]
        for i in range(1, len(nums)):
            if maj == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    maj = nums[i+1]
        
        return maj