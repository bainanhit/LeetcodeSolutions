class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash表法
        record = dict()
        for idx, num in enumerate(nums):
            if target - num in record:
                return [record[target - num], idx]
            else:
                record[num] = idx
        return None