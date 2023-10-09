class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        i = 0
        j = len(piles) -2

        while j > i:
            total += piles[j]
            j -=2
            i += 1
        return total 


        