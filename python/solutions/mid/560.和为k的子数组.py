class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 + 哈希表
        n = len(nums)
        _map = {}
        _map[0] = 1
        count, pre_sum= 0, 0
        for i in range(0, n):
            pre_sum += nums[i]
            if (pre_sum - k) in _map:
                count += _map[pre_sum-k]
            _map[pre_sum] = _map.get(pre_sum, 0) + 1
            
        return count
                
            
            

