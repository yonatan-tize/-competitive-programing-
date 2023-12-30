class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        size = len(piles)
        l = size // 3
        r = size - 2
        while r >= l:
            ans += piles[r]
            r -= 2
        return ans