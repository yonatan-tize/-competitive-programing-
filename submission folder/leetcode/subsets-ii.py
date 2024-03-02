class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()

        def backtrack(index, curr):
            subsets.append(curr[:])
            if index == len(nums):
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue 
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])

        return subsets