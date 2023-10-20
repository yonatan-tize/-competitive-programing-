class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        size = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] not in a or a[s[right]] < left:
                a[s[right]] = right
                size = max(size, right-left + 1)
            else:
                left = a[s[right]] + 1
                a[s[right]] = right
            right += 1
        return size