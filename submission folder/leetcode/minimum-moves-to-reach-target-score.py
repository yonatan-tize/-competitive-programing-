class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num_moves = 0

        while target != 0:

            if maxDoubles > 0 and target > 1:

                if target % 2 == 0:
                    num_moves += 1
                else:
                    num_moves += 2

                maxDoubles -= 1 
                target //= 2

            else:
                num_moves += (target-1)
                return num_moves 

        return num_moves
