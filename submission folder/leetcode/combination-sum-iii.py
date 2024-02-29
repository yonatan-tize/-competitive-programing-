class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        ans = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
        def helper(candidates, index, curr, total):
            if index == len(candidates):
                if len(curr) == k and total == target:
                    ans.append(curr[:])
                return 

            if len(curr) == k:
                if total == target:
                    ans.append(curr[:])
                    return
                return 

            if total > target:
                return 


            curr.append(candidates[index])
            helper(candidates, index + 1, curr, total + candidates[index])
            curr.pop()
            helper(candidates, index + 1, curr, total)

        helper(candidates, 0, [], 0)
        return ans