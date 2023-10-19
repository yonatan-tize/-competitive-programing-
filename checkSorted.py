class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        l, r = 0, 1
        
        while r < n:
            if arr[r] < arr[l]:
                return 0
            r += 1
            l += 1
        return 1