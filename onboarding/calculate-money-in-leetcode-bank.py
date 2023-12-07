class Solution:
    def totalMoney(self, n: int) -> int:
        w1 = 28
        totalWeeks = n // 7
        remainingDays = n % 7

        weeks = totalWeeks * (2 * w1 + (totalWeeks-1) * 7)  // 2
        days = remainingDays * (2 * (totalWeeks + 1) + (remainingDays-1) * 1) // 2
        return weeks + days




