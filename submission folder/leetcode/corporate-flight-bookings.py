class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        psum = [0] * n
        for first, last, seats in bookings:
            psum[first-1] += seats
            if last < n:
                psum[last] -= seats

        for i in range(1, n):
            psum[i] += psum[i-1]

        return psum
