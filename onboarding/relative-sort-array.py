class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans1 = []
        ans2 = []
        for num in arr2:
            for i in range(count[num]):
                ans1.append(num)
                del count[num]
        for key, value in count.items():
            for i in range(value):
                ans2.append(key)
        ans2.sort()
        ans1.extend(ans2)
        return ans1
