class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(n):
            if n <= 1: 
                return 1

            return n * factorial(n-1)

        ans = []
        for i in range(rowIndex+1):
            t = factorial(rowIndex) / (factorial(i) * factorial(rowIndex-i))
            ans.append(int(t))

        return ans
            