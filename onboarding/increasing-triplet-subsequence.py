class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        max1 = float('inf')
        max2 = float('inf')
        for num in nums:
            if num <= max1:
                max1 = num
            elif num <= max2:
                max2 = num
            else:
                return True 
        return False
        
        
         
        