class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        preSum = [0] * len(s)
        ans = ''

        for start, end, direction in shifts:
            if direction == 0:
                preSum[start] += -1
                if end < len(s)-1: preSum[end+1] -= -1
            else:
                preSum[start] += 1
                if end < len(s)-1: preSum[end+1] -= 1
        
        for i in range(1,len(preSum)):
            preSum [i] += preSum[i-1]

        for i, char in enumerate(s):
            if preSum[i] < 0:
                preSum[i] += 26
            ans += chr(((ord(char) - ord('a') + preSum[i]) % 26 ) + 97)

        return ans