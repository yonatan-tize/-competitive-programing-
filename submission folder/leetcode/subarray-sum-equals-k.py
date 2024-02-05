class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0:1}
        ans = 0
        psum = 0
        for i in nums:
            psum += i  
            if psum-k in sum_dict:
                ans += sum_dict[psum-k]

            sum_dict[psum] = sum_dict.get(psum, 0) + 1

        return ans 