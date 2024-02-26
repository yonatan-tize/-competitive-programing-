# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        left = 0
        right = 0

        if root.left:
            root.left.val  += (root.val * 10)
            left = self.sumNumbers(root.left)

        if root.right:
            root.right.val += (root.val * 10)
            right = self.sumNumbers(root.right)  

        return right + left