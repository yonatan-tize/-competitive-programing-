class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        psum = [0] * (len(nums)+2)
        for i,num  in enumerate(nums):
            psum[i+1] = psum[i] + num

        for i in range(1, len(psum)-1):
            if psum[i-1] == psum[-2] - psum[i]:
                return i-1

        return -1
           

            