class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a = [0] * 50

        for start, end in ranges:
            a[start-1] += 1
            if end < 50:
                a[end] -= 1
        for i in range(len(a)):
            if i > 0:
                a[i] += a[i-1]
            if i in range(left-1, right):
                if a[i] == 0:
                    return False
        return True