class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        #  这里控制条件没取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            # 中间数字等于右边数字，比如[2,3,1,1,1]或者[4,1,2,3,3,3]
            # 则重复数字可能为最小值，也可能最小值在重复值的左侧
            # 所以将right左移一位
            else:
                r -= 1

        return nums[l]