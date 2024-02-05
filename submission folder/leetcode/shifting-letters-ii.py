class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        psum = [0] * len(s)
        for start, end, dxn in shifts:
            if dxn == 0:
                psum[start] -= 1
                if end < len(s)-1:
                    psum[end+1] += 1
            else:
                psum[start] += 1
                if end < len(s)-1:
                    psum[end+1] -= 1

        for i in range(1, len(s)):
            psum[i] += psum[i-1]

        ans = ''
        for i, char in enumerate(s):
            if psum[i] < 0:
                psum[i] += 26
            ans += chr(((ord(char) - ord('a') + psum[i]) % 26) + 97)

        return ans
        