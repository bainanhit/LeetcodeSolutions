class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cnt = m + n - 1
        m -= 1
        n -= 1
        
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[cnt] = nums1[m]
                cnt -= 1
                m -= 1
            else:
                nums1[cnt] = nums2[n]
                cnt -= 1
                n -= 1
        while n >= 0:
            nums1[cnt] = nums2[n]
            cnt -= 1
            n -= 1
        
    
         