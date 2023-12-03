class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        words = s.split()
        for i in range(len(max(words, key = lambda x: len(x)))):
            ver_word = ''
            for word in words:
                if i < len(word):
                    ver_word += word[i]
                else:
                    ver_word += " "
            ver_word = ver_word.rstrip()
            ans.append(ver_word)
        return ans