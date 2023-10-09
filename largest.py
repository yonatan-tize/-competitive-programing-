class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)

        def compare(nums1, nums2):
            if nums1 + nums2 > nums2 + nums1:
                return -1
            else:
                return 0        
        nums = sorted(nums,key= cmp_to_key(compare))
               
        largest_num = ''.join(nums)

        if largest_num[0] == '0':
            return '0'

        return largest_num


        