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
    

        # 法二
        def quicksort():
            def quick_sort(arr, l, r):
                # 子数组长度为 1 时终止递归
                if l >= r: return
                # 哨兵划分操作（以 arr[l] 作为基准数）
                i, j = l, r
                while i < j:
                    while i < j and arr[j] >= arr[l]: j -= 1
                    while i < j and arr[i] <= arr[l]: i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                arr[l], arr[i] = arr[i], arr[l]
                # 递归左（右）子数组执行哨兵划分
                quick_sort(arr, l, i - 1)
                quick_sort(arr, i + 1, r)
            
            quick_sort(arr, 0, len(arr) - 1)

