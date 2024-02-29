class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minimum = float('inf')

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True

            stack.append([num, minimum])
            minimum = min(minimum, num)

        return False

