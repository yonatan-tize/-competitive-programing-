class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_position = {}
        # store every character with their index
        for i, num in enumerate(nums):
            num_position[num] = i

        for i, replacing in operations:
            index = num_position[i]
            nums[index] = replacing
            num_position[replacing] = index
        return nums


        