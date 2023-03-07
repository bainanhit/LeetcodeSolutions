class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 递归二分
        m, n = len(nums1), len(nums2)
        # 两个数组长度为奇数：中位数就是第(m+n)/2+1小元素；两个数组长度为偶数：中位数是第(m+n)/2小与第(m+n)/2+1小元素的和的一半，故分解为两个0.5来处理
        left = (n+m+1) // 2
        right = (n+m+2) // 2
        # 将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k
        return (self.getKthMin(nums1, 0, m-1, nums2, 0, n-1, left)+self.getKthMin(nums1, 0, m-1, nums2, 0, n-1, right))*0.5
    
    def getKthMin(self, nums1, start1, end1, nums2, start2, end2, k):
        len1, len2 = end1 - start1 + 1, end2-start2+1
        # 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1 
        if len1 > len2:
            return self.getKthMin(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        # 为了防止数组长度小于 k/2，所以每次比较 min(k/2，len(数组) 对应的数字
        i = start1 + min(len1, k//2) - 1
        j = start2 + min(len2, k//2) - 1
        if nums1[i] > nums2[j]:
            return self.getKthMin(nums1, start1, end1, nums2, j+1, end2, k-(j-start2+1))
        else:
            return self.getKthMin(nums1, i+1, end1, nums2, start2, end2, k-(i-start1+1))
        
        

