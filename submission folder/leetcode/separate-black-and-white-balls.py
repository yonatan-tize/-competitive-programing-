class Solution:
    def minimumSteps(self, s: str) -> int:
        l = len(s)-1
        r = len(s)-1
        s = list(s)
        count = 0
        while l >= 0:
            while l >= 0 and s[l] == '0':
                l -= 1
            while r >= 0 and s[r] == '1':
                r -= 1

            if l >= 0 and l < r:
                count += (r-l)
                s[r], s[l] = s[l], s[r]
                r -= 1
            l -= 1

        return count


            