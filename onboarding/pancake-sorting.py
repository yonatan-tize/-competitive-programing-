class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def maximum(arr, start, end):
            ans = 0
            index = 0
            while start <= end:
                if arr[start] > ans: 
                    ans = arr[start]
                    index = start
                start += 1
            return index
        def swap(arr, i , j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        ans = []
        last_index = len(arr)-1
        ordered = sorted(arr)
        i = 0
        while arr != ordered:
            maxIndex = maximum(arr, 0, last_index)
            swap(arr, 0, maxIndex)
            swap(arr, 0, last_index)
            ans.append(maxIndex + 1)
            ans.append(last_index + 1)
            last_index -= 1
            if last_index == -1:
                break
        return ans        