class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        possible_ans = 1
        i, j = 0, 1

        while j < n:
            if arr[j] == arr[j-1]:
                i = j
            elif j == n-1 or (arr[j] - arr[j-1]) *  (arr[j] - arr[j+1]) <= 0:
                possible_ans = max(j - i + 1, possible_ans)
                i = j 
            j += 1

        return possible_ans