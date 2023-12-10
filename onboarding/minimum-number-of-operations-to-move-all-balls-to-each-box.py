class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_ones = {}
        for i,n in enumerate(boxes):
            if n == '1':
                index_ones[i] = n
        ans = []
        for i,n in enumerate(boxes):
            count = 0
            for key, value in index_ones.items():
                count += abs(i-key)
            ans.append(count)
        
        return ans

        