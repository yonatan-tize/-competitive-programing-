class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        nums.extend(nums) 
        stack = []
        for i, num in enumerate(nums):
            if stack:
                while stack and num > stack[-1][0]:
                    n = stack.pop()
                    if n[1] < len(ans):
                        ans[n[1]] = num

                stack.append([num, i])

            else:
                stack.append([num, i])

        # while stack:
        #     if len(stack) > 1 and stack[-1][0] < stack[0][0]:
        #         num, index = stack.pop()
        #         ans[index] = stack[0][0]
        #     else:
        #         break

        return ans

        

                