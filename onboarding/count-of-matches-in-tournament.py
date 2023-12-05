class Solution:
    def numberOfMatches(self, n: int) -> int:
        number_games = 0
        while n > 1:
            if n % 2 == 0:
                number_games += n / 2
                n /= 2
            else:
                number_games += (n - 1) / 2
                n = (n - 1) / 2 + 1
        return int(number_games)

