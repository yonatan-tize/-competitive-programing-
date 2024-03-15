class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (right + left) // 2
                if nums[mid][0] > target:
                    right = mid - 1
                elif nums[mid][0] < target:
                    left = mid + 1
                else:
                    return nums[mid][1]

            return nums[left][1] if left < len(nums) else -1

        index = [[nums[0], i] for i,nums in enumerate(intervals)]
        index.sort()
        print(index)
        ans = []
        for start, end in intervals:
            i = binarySearch(index, end)
            ans.append(i)

        return ans



        
