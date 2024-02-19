class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = defaultdict(lambda : -1)
        stack = [] 
        for num in nums2:
            while stack and num > stack[-1]:
                store[stack[-1]] = num
                stack.pop()

            stack.append(num)

        return [store[num] for num in nums1]