class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] < l and i != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
            else:
                i += 1
        for j in range(len(nums)):
            if j != nums[j]:
                return j
        return len(nums)
                















        nums.sort()
        for i,num in enumerate(nums):
            if num != i:
                return i
        return len(nums)