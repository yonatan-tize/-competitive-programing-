class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        def distance(nums):
            n = len(nums)
            psum = [0] * (n+2)
            psum[1] = nums[0]
            for i in range(1, n):
                psum[i+1] += nums[i] + psum[i]

            ans = []
            for i, num in enumerate(nums):
                left = nums[i] * i - psum[i] 
                right = psum[-2] - psum[i+1] - (n-i-1) * nums[i]
                dist = left + right
                ans.append(dist)
            
            return ans

        store = defaultdict(list)
        for i, num in enumerate(arr):
            store[num].append(i)

        for key, value in store.items():
            store[key] = distance(value)
        print(store)
        ans = [0] * len(arr)
        for j in range(len(arr) - 1, -1, -1):
            a = store[arr[j]]
            ans[j] = a[-1]
            store[arr[j]].pop()

        return ans

        




