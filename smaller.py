class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ans = list()
        for num in nums:
            index = arr.index(num)
            ans.append(index)
        return ans

        