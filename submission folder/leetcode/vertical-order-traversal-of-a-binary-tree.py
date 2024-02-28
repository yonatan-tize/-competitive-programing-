# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)

        def helper(root, row, col):

            if not root:
                return 

            store[col].append((root.val,row))

            helper(root.left, row+1, col - 1)
            helper(root.right, row+1, col + 1)
        helper(root, 0 , 0)

        answer = []

        for key in sorted(store.keys()):
            nodes = [val for val,row in sorted(store[key],key = lambda x : (x[1],x[0]))]
            answer.append(nodes)
        return answer
   


        



