class Solution: 
    def select(self, arr, i):
        maxnum = -float('inf')
        index = 0
        for j in range(i):
            if arr[j] > maxnum:
                maxnum = arr[j]
                index = j
        return index
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            max_index = self.select(arr, n-i)
            arr[max_index], arr[n-i-1] = arr[n-1-i], arr[max_index] 
        return arr