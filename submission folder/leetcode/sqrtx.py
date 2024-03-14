class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        start = 1
        end = x // 2

        while start <= end:
            mid =(start + end) // 2
            if mid ** 2 == x or (mid ** 2 < x and (mid + 1) ** 2 > x):
                return mid

            elif mid ** 2 > x:
                end = mid - 1

            else:
                start = mid + 1

        return -1
