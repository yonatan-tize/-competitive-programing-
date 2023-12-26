class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        currMax = flips[0]
        count = 0
        for i in range(len(flips)):
            currMax = max(currMax, flips[i])
            if currMax == i+1:
                count += 1
        return count
            
