class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked = set()
        n = len(nums)
        for i, num in enumerate(nums):
            if i in checked:
                continue
            cycle_set = set()
            while True:
                if i in cycle_set: # that means we have seen it before so that is cycle
                    return True

                checked.add(i)
                cycle_set.add(i)
                prev, i = i, (i + nums[i]) % n
                if prev == i: # to check if it is uni-cycle(cycle around self) 
                    break
                if nums[i] * num < 0:
                    break
        return False
            
                


                    



