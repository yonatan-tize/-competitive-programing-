class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        store ={}
        for i, num in enumerate(a):
            if num not in store:
                store[num] = i
        ans = []
        for n in nums:
            ans.append(store[n])
        return ans
