class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        ans = ''
        for i in range(len(s)):
            for word in strs:
                if i < len(word) and word[i] == s[i]:
                    continue
                else:
                    return ans
            ans += word[i]
        return ans
