class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            if target-num in store:
                return [i, store[target-num]]
            else:
                store[num] = i
        return [0,0]