class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = dict()

        for i, char in enumerate(s):
            lastIndex[char] = i
        ans = []
        l, r = 0, 0
        m = 0

        while r < len(s):
            m = max(m, lastIndex[s[r]])

            if r == m:
                ans.append(r-l+1)
                l = r + 1
            r += 1
        return ans
        