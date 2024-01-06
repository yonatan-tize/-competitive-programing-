class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_num = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if abs(target - three_sum) < closest_num:
                    closest_num = abs(target - three_sum)
                    ans = three_sum
                if three_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans
                
