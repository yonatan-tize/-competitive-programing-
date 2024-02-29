# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums):
            if len(nums) == 0:
                return None
            
            maxi = max(nums)
            index = nums.index(maxi)

            return TreeNode(maxi, helper(nums[:index]), helper(nums[index+1:]))

        return helper(nums)