class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(curr, nums, l):
            if l == len(nums):
                ans.append(curr[:])
                return 
            
            n = nums[l]
            for i in range(len(curr)+1):
                curr.insert(i, n)
                helper(curr, nums, l + 1)
                curr.remove(n)

        helper([], nums, 0)
        return ans

