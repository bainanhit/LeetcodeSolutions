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
    

    # 法二
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        map = {}
        cnt = 0
        psum = [0]*(n+1)
        # 求前缀和数组，注意前缀和数组要比原数组多一个首位的0
        for i in range(1, n+1):
            psum[i] = nums[i-1] + psum[i-1]
        # map: key-前缀和, value-前缀和为key的个数
        # 一次遍历，每次遍历既要根据当前数查找哈希表，又要将遍历到的数存入哈希
        for i in range(n+1):
            # 如果有与当前 sums[i] 差为 k 的则加上它的个数
            if (psum[i]-k) in map:
                cnt += map[psum[i]-k]
            map[psum[i]] = map.get(psum[i], 0) + 1

        return cnt


    
            
            

