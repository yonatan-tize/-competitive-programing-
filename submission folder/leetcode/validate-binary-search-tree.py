# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, mini, maxi):
            if not root:
                return True

            if root.val >= maxi or root.val <= mini:
                return False


            return helper(root.left, mini, root.val) and helper(root.right, root.val, maxi)

        return helper(root, -float("inf"), float('inf'))

            