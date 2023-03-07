class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 哈希表， 双指针
        res = 0
        hash_dict = {}
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num-1, 0)
                right = hash_dict.get(num+1, 0)
                # 把当前数加入哈希表
                hash_dict[num] = 1
                length = left+1+right
                res = max(res, length)
                # 更新最左端和最右端的值
                hash_dict[num-left] = length
                hash_dict[num+right] = length
                
        return res
