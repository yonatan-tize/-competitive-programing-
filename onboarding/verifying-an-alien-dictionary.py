class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        characters = {}

        for i in range(26):
            characters[order[i]] = i

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j < len(word1) and j == len(word2):
                    return False
                if characters[word1[j]] > characters[word2[j]]:
                    return False
                elif characters[word1[j]] < characters[word2[j]]:
                    break
        return True


