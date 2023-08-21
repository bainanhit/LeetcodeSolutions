class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 快速划分
        # 0(n) Z(logn)
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i<j and arr[j] >= arr[l]:
                    j -= 1
                while i<j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]

            arr[l], arr[i] = arr[i], arr[l]
            # pivot为arr[i]，划分为左右两个区间
            if k<i: return quick_sort(l, i-1)
            if k>i: return quick_sort(i+1, r)
            # 若k=i，则arr[k]为第k+1小的数字
            return arr[:k]
        
        return quick_sort(0, len(arr)-1)
