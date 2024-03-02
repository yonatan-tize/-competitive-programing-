class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(index, curr, total):
            if total == target:
                combinations.append(curr[:])
                return 

            if total > target or index == len(candidates):
                return 

            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                backtrack(i , curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return combinations

