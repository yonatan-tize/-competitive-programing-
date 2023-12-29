class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = lambda x: x[-1])
        ans = ''
        for word in s:
            ans += ' ' +  word[:-1]
        return ans.lstrip()