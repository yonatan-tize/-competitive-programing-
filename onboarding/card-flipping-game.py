class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        ans = float('inf')
        repeated = set(front for front, back in zip(fronts, backs) if front == back)

        for j in range(len(fronts)):
            if fronts[j] not in repeated:
                ans = min(ans, fronts[j])
            if backs[j] not in repeated:
                ans = min(ans, backs[j])
        return ans if ans != float('inf') else 0

        