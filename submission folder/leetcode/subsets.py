class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(curr, nums, l):
            if l == len(nums):
                ans.append(curr[:])
                return 
            curr.append(nums[l])
            helper(curr, nums, l + 1)
            curr.pop()
            helper(curr, nums, l + 1)

        helper([], nums, 0)

        return ans

            