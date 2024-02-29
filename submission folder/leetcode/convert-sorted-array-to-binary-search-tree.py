# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums):
            if len(nums) == 0:
                return None
            mid = len(nums) // 2
            return TreeNode(nums[mid], helper(nums[:mid]), helper(nums[mid+1:]))

        return helper(nums)