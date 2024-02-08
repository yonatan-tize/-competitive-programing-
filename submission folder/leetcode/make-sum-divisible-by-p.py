class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p  
        if target == 0:
            return 0

        print(target)
        store = {0:-1}
        min_window = len(nums)
        curr_sum = 0 
        
        for i in range(len(nums)):
            curr_sum += nums[i]

            if (curr_sum - target) % p in store:
                index = i - store[(curr_sum - target)% p] 
                min_window = min(min_window, index)
            store[curr_sum % p] = i

        return min_window if min_window < len(nums) else -1













   # for i in range(len(nums)):
        #     curr_sum += nums[i]
        #     while curr_sum > target:
        #         curr_sum -= nums[l] 
        #         l += 1

        #     if curr_sum == target:
        #         min_window = min(min_window, i-l+1)

        # return min_window if min_window < len(nums) else -1