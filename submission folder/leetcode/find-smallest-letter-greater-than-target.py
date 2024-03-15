class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)-1

        while start <= end:
            mid = (start + end) // 2
            
            if letters[mid] <= target:
                start = mid + 1

            elif letters[mid] > target:
                end = mid - 1

        if start == len(letters):
            return letters[0]

        return letters[start]