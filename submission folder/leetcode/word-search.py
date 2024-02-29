class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        def helper(index, row, col):
            if index == len(word) or (index + 1 == len(word) and word[index] == board[row][col]):
                return True

            if word[index] != board[row][col] :
                return False
            
            prev = board[row][col]
            board[row][col] = 'visited'
            t1 = t2 = t3 = t4 = False
            if row > 0:  # up
                t1 = helper(index + 1, row - 1, col) 
                if t1:
                    return True

            if row < r-1: # down
                t2 = helper(index + 1, row + 1, col) 
                if t2:
                    return True

            if col < c-1: # right
                t3 = helper(index + 1, row, col + 1)
                if t3:
                    return True

            if col > 0:  # left
                t4 = helper(index + 1, row, col - 1) 
                if t4:
                    return True

            board[row][col] = prev

            return (t1 or t2) or (t3 or t4)

        for row in range(r):
            for col in range(c):
                ans = helper(0, row, col)
                if ans:
                    return True 

                

        
        return False




