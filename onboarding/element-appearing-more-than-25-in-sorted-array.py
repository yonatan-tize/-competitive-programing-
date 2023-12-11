class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        size = len(arr) / 4

        for key, value in count.items():
            if value > size:
                return key
        return -1