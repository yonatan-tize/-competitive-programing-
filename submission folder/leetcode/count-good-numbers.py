class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1) // 2
        odd = n // 2
        MOD = 10 ** 9 + 7

        def power(num, exp): #ans == num

            if exp == 0:
                return 1

            ans =(power(num, exp // 2)) % MOD
            if exp % 2 == 0:
                return (ans * ans) % MOD

            return num * (ans * ans) % MOD


        return (power(5, even) * power(4, odd)) % MOD
