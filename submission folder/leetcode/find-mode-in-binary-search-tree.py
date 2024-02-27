# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        store = defaultdict(int)
        def counter(root):
            if not root:
                return 

            store[root.val] += 1
            counter(root.left)
            counter(root.right)

        counter(root)

        second = defaultdict(list)
        max_key = 0
        for key, value in store.items():
            second[value].append(key)

            max_key = max(max_key, value)

        return second[max_key]

        

        

        
        

