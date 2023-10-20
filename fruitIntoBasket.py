class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        a = {}
        maxFr = 0

        while right < len(fruits):
            a[fruits[right]] = right
            if len(a) <= 2:
                maxFr = max(maxFr, right-left + 1)
                right += 1
            else:
                index = min(value for value in a.values())
                left = a[fruits[index]] + 1
                del a[fruits[index]] 
        return maxFr