class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        MOD =  10 ** 9 + 7
        res = 0

        for i, num in enumerate(arr):
            
            while stack and stack[-1][0] > num:
                n, j = stack.pop()
                left = j - stack[-1][1] if stack else j + 1
                right = i - j

                res = (res + left * right * n) % MOD

            stack.append([num, i])    

        while stack:
            n, j = stack.pop()
            left = j - stack[-1][1] if stack else j + 1
            right = len(arr) - j

            res = (res + left * right * n) % MOD
        
        return res
