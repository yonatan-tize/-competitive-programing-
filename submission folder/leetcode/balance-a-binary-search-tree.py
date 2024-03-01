# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def numbers(root):
            if not root:
                return None

            numbers(root.left)
            nums.append(root.val)
            numbers(root.right)

        numbers(root)
        def buildTree(arr):
            if len(arr) == 0:
                return None
            mid = len(arr) // 2
            return TreeNode(arr[mid], buildTree(arr[:mid]), buildTree(arr[mid+1:]))

        return buildTree(nums)

