class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        up = 'True'
        row = len(mat)
        column = len(mat[0])
        r = 0
        c = 0
        while len(ans) != row * column:
            
            if up:
                while r >= 0 and c < column:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
                if c == column:
                    c -= 1
                    r += 2 
                else:
                    r += 1
                up = False
            else:
                while r < row and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
                if r == row:
                    c += 2
                    r -= 1 
                else:
                    c += 1 
                up = True
        return ans






















        # row = 0
        # col = 0
        # direction = 'UP'
        # # moving rightup -> left -> leftdown -> down -> rightUp
        # while len(ans) < len(mat) * len(mat[0]):
        #     if direction == 'UP': # moving down and rightUp
        #         r = 0
        #         c = 0 
        #         while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        #             ans.append(mat[r][c])
        #             r -= 1
        #             c += 1
        #         direction = 'Right-Down'  
        #     if direction == 'Right-Down': #move Right then leftdown
        #         r = 0
        #         while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        #             ans.append(mat[r][c])
        #             r += 1
        #             c -= 1
        #         direction = 'Down-up' if  c < 0 else 'right-up'
            
        #     if direction == 'Down-up':
        #         c = 0 
        #         while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        #             ans.append(mat[r][c])
        #             r -= 1
        #             c += 1
        #         direction = 'DownLeft' if col >= len(mat[0]) else 'Right-Down' 
        #     if direction == 'right-up':
        #         c += 1 
        #         while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        #             ans.append(mat[r][c])
        #             r -= 1
        #             c += 1
        #         direction = 'Right-Down' if c < len(mat[0]) else 'DownLeft'  
        
        #     if direction == 'DownLeft':
        #         c -= 1
        #         r = 1
        #         while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        #             ans.append(mat[r][c])
        #             r += 1
        #             c -= 1
        #         direction = 'DownRight' if  r < len(mat) else 'Right'
        # return ans

            

