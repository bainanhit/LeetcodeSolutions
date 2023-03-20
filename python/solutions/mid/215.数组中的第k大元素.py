class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快速选择
        # O(N) 近线性  由partition性质决定 
        def partition(nums, left, right):
            i, j = left, right
            pivot = nums[left]
            while i < j:
                while i < j and nums[j] <= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] >= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            return i 
        
        
        def topk_split(nums, k, left, right):
            if left <= right:
                idx = partition(nums, left, right)
                # print(idx, left, right, nums)
                if idx == k-1:
                    return idx  # 返回第 K 个数
                elif idx < k-1:
                    return topk_split(nums, k, idx + 1, right)
                else:
                    return topk_split(nums, k, left, idx - 1)

        return nums[topk_split(nums, k, 0, len(nums)-1)]
    
