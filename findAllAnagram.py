class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        pd = [0] * 26
        sd = [0] * 26

        for char in p:
            pd[ord(char) - ord('a')] += 1

        l, r = 0, len(p)
        size = len(s)

        for char in s[l:r]:
            sd[ord(char) - ord('a')] += 1

        while r <= size:
            if sd == pd:
                result.append(l)

            sd[ord(s[l]) - ord('a')] -= 1
            if r < size:
                sd[ord(s[r]) - ord('a')] += 1

            l += 1
            r += 1

        return result