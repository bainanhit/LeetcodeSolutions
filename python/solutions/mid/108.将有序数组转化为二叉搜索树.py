# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # O(N) Z(logN)
        # 要求平衡， 故使用二分法
        def helper(left, right):
            if left > right:
                return None
            # 选择中间位置左边数字作为根节点
            mid = left + (right-left)//2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        return helper(0, len(nums)-1)

