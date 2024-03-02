class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        seen = set()
        def helper(index, curr, total):
            if total == target:
                    ans.append(curr[:])
                    return

            if total > target or index == len(candidates):
                return 

            for i in range(index, len(candidates)):  
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                helper(i + 1, curr, total + candidates[i])
                curr.pop()

        helper(0, [], 0)
        return ans

            
