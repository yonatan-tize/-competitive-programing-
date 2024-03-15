class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isValid(citaions,target):
            # search the correct position of the h index which is at the most left 
            size = len(citations)
            left = 0
            right = size - 1
            while left <= right:
                mid = (left + right) // 2
                if citations[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            valid_papers = len(citations) - left 
            return valid_papers >= target

        left = 0
        right = 1000

        while left <= right:
            mid = (left + right) // 2
            if isValid(citations, mid):
                ans = left
                left = mid + 1
            else:
                right = mid - 1

        return left-1



