class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        smaller = []
        equal = []
        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot:
                smaller.append(num)
            else:
                equal.append(num)
        smaller.extend(equal)
        smaller.extend(greater)
        return (smaller)



