class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        seen = set()
        def helper(curr, nums, l):
            
            if l == len(nums):
                if not tuple(curr[:]) in seen:
                    seen.add(tuple(curr[:]))
                    ans.append(curr[:])
                    return 
                else:
                    return 

            curr.append(nums[l])
            helper(curr, nums, l+1)
            curr.pop()
            helper(curr, nums, l+1)

        helper([], nums, 0)
        return ans
