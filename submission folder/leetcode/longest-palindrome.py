class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_one = 1
        amount = Counter(s)
        ans = 0

        for value in amount.values():
            if value % 2 == 0:
                ans += value

            else:
                if count_one:
                    ans += value
                    count_one -= 1
                else:
                    ans += value-1

        return ans

