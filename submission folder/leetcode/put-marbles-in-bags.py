class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        contribution = []

        for i in range(1, len(weights)):
            contribution.append(weights[i] + weights[i-1])

        contribution.sort()
        l = len(contribution)-k+1
        
        return sum(contribution[l:]) - sum(contribution[:k-1])
