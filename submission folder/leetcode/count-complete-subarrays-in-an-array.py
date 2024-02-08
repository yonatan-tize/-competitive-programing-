class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        store = defaultdict(int)
        l = 0
        count = 0
        for i in range(len(nums)):
            store[nums[i]] += 1 

            while len(store) == distinct:
                count += len(nums)-i
                store[nums[l]] -= 1
                if store[nums[l]] == 0:
                    del store[nums[l]]
                l += 1

        return count



