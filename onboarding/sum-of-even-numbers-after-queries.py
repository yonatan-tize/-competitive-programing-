class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        ans = []
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        for val, index in queries:
            if nums[index] % 2 == 0:
                if val %2 == 0:
                    even_sum += val
                    nums[index] += val
                else:
                    even_sum -= nums[index]
                    nums[index] += val
            else:
                if val %2 == 0:
                    nums[index] += val
                else:
                    nums[index] += val
                    even_sum += nums[index]
            ans.append(even_sum)
        return ans
        


        