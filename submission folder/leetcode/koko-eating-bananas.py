class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(piles, hour, cap):
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / cap)

            return curr_h <= hour

        left = 1
        right = max(piles)

        while left <= right:
            mid = (right + left) // 2
            if isValid(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

