class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        store = {0:1}
        psum = 0
        total = 0
        for num in nums:
            psum += num
            if psum - goal in store:
                total += store[psum - goal]
            store[psum] = store.get(psum, 0) + 1
        return  total