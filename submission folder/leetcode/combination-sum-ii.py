class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        seen = set()
        def helper(index, curr, total):

            if index == len(candidates):
                if total == target:
                    ans.append(curr[:])
                    return
                return 

            if total == target:
                ans.append(curr[:])
                return

            if total > target:
                return

            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue

                curr.append(candidates[i])
                helper(i + 1, curr, total + candidates[i])
                curr.pop()
                prev = candidates[i]

        helper(0, [], 0)
        return ans

            
