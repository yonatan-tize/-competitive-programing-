# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, maxi, mini):
            if not root:
                return maxi - mini 

            maxi = max(maxi, root.val)
            mini = min(mini, root.val)

            left = helper(root.left, maxi, mini)
            right = helper(root.right, maxi, mini)

            return max(left, right)
        
        return helper(root, root.val, root.val)

            