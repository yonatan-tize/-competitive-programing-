class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        max_len = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in count or count[s[i]] < l:
                count[s[i]] = i
                max_len = max(max_len, i-l+1)
            else:
                l = count[s[i]] + 1
                count[s[i]] = i
        return max_len 

