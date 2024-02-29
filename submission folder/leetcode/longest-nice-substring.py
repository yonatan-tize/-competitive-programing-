class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(st):
            chars = set(st)
            if len(chars) < 2:
                return ''

            for i, char in enumerate(st):
                if not (char.lower() in chars and char.upper() in chars):
                    s1 = helper(st[:i])
                    s2 = helper(st[i+1:])
                    return s1 if len(s1) >= len(s2) else s2

            return st
        return helper(s)