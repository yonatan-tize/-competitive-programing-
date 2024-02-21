class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = nums[-1]
        count = 0

        for i in range(len(nums)-2, -1, -1):

            if nums[i] > n:
                num_bucket = math.ceil(nums[i] / n)
                count += (num_bucket - 1) 
                n = nums[i] // num_bucket
            else:
                n = nums[i]

        return count

