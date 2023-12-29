class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if s[j] + s[j+1] < s[j+1] + s[j]:
                    s[j], s[j+1] = s[j+1], s[j]
        if s[0] == '0':
            return '0'
        return ''.join(s) 