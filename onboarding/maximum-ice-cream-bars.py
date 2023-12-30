class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        total = 0
        for c in costs:
            total += c
            if total > coins:
                return count
            count += 1
        return count