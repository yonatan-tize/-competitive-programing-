class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        store= []
        for row in matrix:
            store.append(row[-1])

        def binarySearch(nums, target):
            left = 0
            right = len(nums)-1

            while left <= right:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    right = mid - 1

                else:
                    left = mid + 1

            return left

        row = binarySearch(store, target)
        if row < len(matrix):
            i = binarySearch(matrix[row], target)
            if i < len(matrix[row]):
                return matrix[row][i] == target
        return False

        
