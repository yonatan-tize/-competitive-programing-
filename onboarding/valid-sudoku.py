class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for every row
        for row in board:
            store= set()
            for num in row:
                if num in store:
                    return False
                if num != '.':
                    store.add(num) 
        print(store)
        
        # for every column
        for col in range(9):
            store = set()
            for row in range(9):
                if board[row][col] in store:
                    return False
                if board[row][col] != '.':
                    store.add(board[row][col])
        print(store)
        # for 3 * 3 part
        for r in range(0, 9, 3):  
            for c in range(0, 9, 3):
                store = set()
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        if  board[i+r][c+j] in store:
                            return False
                        if board[i+r][c+j] != '.':
                            store.add( board[r+i][c+j])
                        j += 1
                    i += 1
        print(store)
        return True




        