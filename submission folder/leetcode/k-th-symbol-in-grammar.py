class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def helper(n, k):
            if n == 1:
                return 0

            if k % 2 == 0:
                num = helper(n-1, math.ceil(k / 2))
                return  1 if num == 0 else 0
            
            else:
                return helper(n-1, math.ceil(k / 2))

        return helper(n, k)


        