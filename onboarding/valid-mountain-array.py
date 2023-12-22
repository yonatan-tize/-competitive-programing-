class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr)-1:
            if arr[i+1] > arr[i]:
                i += 1
            else:
                break
        print(i)
        j = len(arr)-1
        while j > 1:
            if arr[j] < arr[j-1]:
                j -= 1
            else:
                break
        print(j)
        if i != 0 and j != len(arr)-1 and i ==j:
            return True
        return False