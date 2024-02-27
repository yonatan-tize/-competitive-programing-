class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backTrack(candidate):
            if len(candidate) == k:
                return ans.append(candidate[:])

            last = candidate[-1] if candidate else 0

            for i in range(last+1, n+1):
                 candidate.append(i)
                 backTrack(candidate)
                 candidate.pop()

            
        backTrack([])
        return ans

