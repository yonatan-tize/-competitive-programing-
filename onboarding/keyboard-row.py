class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["zxcvbnm", "asdfghjkl", "qwertyuiop"]
        ans = []

        for word in words:
            for row in rows:
                s = ''
                lower_word = word.lower()
                for char in lower_word:
                    if char not in row:
                        break
                    else:
                        s += char
                if s == lower_word:
                    ans.append(word)
                    break
        return ans

                