class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(num, weights, days):
            day = 1
            curr_sum = 0
            for weight in weights:
                
                if weight + curr_sum > num:
                    curr_sum = 0
                    day += 1
                
                curr_sum += weight

            return day <= days

        left = max(weights)
        right = 2**32

        while left <= right:
            mid = (right + left) // 2
            
            if isValid(mid, weights, days):
                right = mid - 1
            else:
                left = mid + 1

        return left
            
