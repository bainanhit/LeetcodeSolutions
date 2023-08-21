class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 归并
        # o(nlogn) z(n)
        if not nums:
            return 0
        res = 0
        def mergesort(l, r):
            if l < r:
                mid = (l+r) // 2
                mergesort(l, mid)
                mergesort(mid+1, r)
                merge(l, r)


        def merge(left, right):    
            nonlocal res
            mid = (left+right) // 2
            l, r = left, mid+1

            tmp = []
            
            while l <= mid and r <= right:
                if nums[l] <= nums[r]:
                    tmp.append(nums[l])
                    l += 1
                else:
                    tmp.append(nums[r])
                    r += 1
                    # 计算逆序数
                    res += mid-l+1

            if l <= mid:
                tmp.extend(nums[l: mid+1])
            else:
                tmp.extend(nums[r:])
            
            nums[left : right+1] = tmp[:]

        l, r = 0, len(nums)-1
        mergesort(l, r)
        return res
            

            
# 内存简化版
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1 # 统计逆序对
            return res
        
        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)