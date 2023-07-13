class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def partition(nums, l, r):
            i, j = l, r
            pivot = nums[i]
            while i < j:
                while i<j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i<j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            return i
        
        def quicksort(nums, l, r):
            if l < r:
                idx = partition(nums, l, r)
                quicksort(nums, l, idx-1)
                quicksort(nums, idx+1, r)
            return nums
        
        return quicksort(nums, 0, n-1)