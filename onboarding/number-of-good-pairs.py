class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    
        count = Counter(nums)
        ans = 0
        for key in count.keys():
            n = count[key]
            ans += (n*(n-1)/2)
        return int(ans)




        
        # count = 0
        # for i in range(len(nums)):
        #     num = nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == num:
        #             count += 1
        # return count