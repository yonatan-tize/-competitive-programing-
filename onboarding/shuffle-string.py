class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [0] * len(s)
        for i in range(len(s)):
            char = s[i]
            index = indices[i]
            answer[index] = char
        return ''.join(answer)