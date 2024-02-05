class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)):
             nums[i] += nums[i-1]

        return nums









        for num in nums:
            curr_sum += num
            running_sum.append(curr_sum)
        return running_sum
