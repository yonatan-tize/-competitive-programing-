class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for col in range(len(matrix[0])):
            a = []
            for row in range(len(matrix)):
                a.append(matrix[row][col])
            ans.append(a)
        return ans