class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = 0
        j = len(num) - 1
        while j >= 0 and int(num[j]) % 2 == 0:
            j -= 1
        return num[i:j+1]

            