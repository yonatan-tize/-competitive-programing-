class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def binarySearch(heaters, target):
            left = 0
            right = len(heaters)-1

            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left
        heaters.sort()
        size = len(heaters) 
        maxi = -float('inf')
        for num in houses:
            index = binarySearch(heaters, num)
            if index == 0:
                maxi = max(maxi, abs(num-heaters[0]))

            elif index == size:
                maxi = max(maxi, abs(num-heaters[-1]))

            else:
                curr = min(abs(num-heaters[index-1]), abs(num-heaters[index]))
                maxi = max(maxi, curr)

        return maxi



