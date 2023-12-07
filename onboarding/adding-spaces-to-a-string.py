class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = spaces[0]
        j =0
        answer = ''
        for i, char in enumerate(s):
            if i == index:
                answer += ' '
                j += 1
                if j < len(spaces):
                    index = spaces[j]
            answer += char
        return answer