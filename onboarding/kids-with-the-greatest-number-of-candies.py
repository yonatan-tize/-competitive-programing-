class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = []
        for num in candies:
            if num + extraCandies >= m:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        