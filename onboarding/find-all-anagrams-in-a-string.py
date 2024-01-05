class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        store = Counter(p)
        anagram = {}
        n = len(p)
        ans = []
        for i in range(n-1):
            anagram[s[i]] = anagram.get(s[i], 0) + 1

        for j in range(n-1, len(s)):
            anagram[s[j]] = anagram.get(s[j], 0) + 1
            if anagram == store:
                ans.append(j-n+1)
                
            anagram[s[j-n+1]] -= 1
            if anagram[s[j-n+1]] == 0:
                del anagram[s[j-n+1]]
                
        return ans
            


             