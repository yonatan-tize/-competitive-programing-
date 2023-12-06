class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        appear = len(nums) / 3

        for key, value in count.items():
            if value > appear:
                ans.append(key)
        return ans