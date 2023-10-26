class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for n in range(1,len(nums)):
            self.nums[n] += self.nums[n-1] 
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.nums[right] - self.nums[left-1]
        return self.nums[right]