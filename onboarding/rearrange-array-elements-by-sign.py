class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        p = 0
        n = 1
        for num in nums:
            if num > 0:
                ans[p] = num
                p += 2
            else:
                ans[n] = num
                n += 2
        return ans

