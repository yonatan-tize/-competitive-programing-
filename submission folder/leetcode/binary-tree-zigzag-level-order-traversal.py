# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        dxn = "left"

        while queue:
            curr = []
            if dxn == 'left': # pop left and append right
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        curr.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                        
                if curr:
                    ans.append(curr)

                dxn = 'right'
            else:
                for i in range(len(queue)):
                    node = queue.pop()
                    if node:
                        curr.append(node.val)
                        queue.appendleft(node.right)
                        queue.appendleft(node.left)

                if curr:
                    ans.append(curr)

                dxn = 'left'

        return ans


                    

                



