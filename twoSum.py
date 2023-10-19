class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            tsum = numbers[i] + numbers[j]
            if tsum == target:
                return [i+1,j+1]
            elif tsum > target:
                j -= 1
            else:
                i += 1
        return [0,0] 
        