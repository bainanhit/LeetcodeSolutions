class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 哈希表， 双指针
        # 时间 空间复杂度 都是O(N)
        '''
        用哈希表存储每个端点值对应连续区间的长度
        若数已在哈希表中：跳过不做处理
        若是新数加入：
            取出其左右相邻数已有的连续区间长度 left 和 right
            计算当前数的区间长度为：cur_length = left + right + 1
            根据 cur_length 更新最大长度 max_length 的值
            更新区间两端点的长度值
        '''
        res = 0
        hash_dict = {}
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num-1, 0)
                right = hash_dict.get(num+1, 0)
                
                cur_len = left+1+right
                res = max(res, cur_len)
                # 把当前数加入哈希表
                hash_dict[num] = cur_len
                # 更新最左端和最右端的值
                hash_dict[num-left] = cur_len
                hash_dict[num+right] = cur_len
                # 此时 【num-left，num-right】范围的值都连续存在哈希表中了
                # 不需要更新区间值，因为用不到
        return res
