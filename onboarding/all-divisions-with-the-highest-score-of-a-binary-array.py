class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count1 = sum(nums)
        count0 = 0
        store = defaultdict(list)
        store[count1].append(0) 
        ans = count1

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            else:
                count1 -= 1
            divScore = count0 + count1
            store[divScore].append(i+1) 
            ans = max(ans, divScore)
            
        return store[ans]


