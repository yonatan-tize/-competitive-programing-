class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = {0:1}
        psum = 0
        ans = 0
        for i, num in enumerate(nums):
            psum += num 
            if psum % k in store:
                ans += store[psum % k]

            store[psum % k] = store.get(psum % k, 0) + 1

        return ans 
