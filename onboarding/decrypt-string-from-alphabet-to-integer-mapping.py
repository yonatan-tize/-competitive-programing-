class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = ''
        n = len(s)
        while i < n:
            if i < n-2 and s[i+2] == '#':
                ans += chr(ord('a') + int(s[i:i+2])- 1)
                i += 3
            else:
                ans += chr(ord('a') + int(s[i])- 1)
                i += 1
        return ans
