class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序 + 双指针
        # 先排序 T=O(nlogn)
        res = []
        n = len(nums)
        nums.sort(reverse=False)
        for k in range(0, n):
            # 剪枝nums[k],排序之后如果第一个元素已经大于零，那么不可能凑成三元组
            if nums[k] > 0:
                break
            # 三元组元素a去重
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            i, j = k+1, n-1
            while i < j:
                tmp = []
                sum = nums[k] + nums[i] + nums[j]
                if sum == 0:
                    tmp.append(nums[k])
                    tmp.append(nums[i])
                    tmp.append(nums[j])
                    res.append(tmp)
                    
                    # 三元组去重b,c
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif sum < 0:
                    i += 1
                else:
                    j -= 1
            
        return res