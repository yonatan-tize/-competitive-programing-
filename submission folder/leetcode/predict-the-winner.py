class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        
        def max_scores(i, j):
            if i > j:
                return 0, 0
            
            if i == j:
                return nums[i], 0

            p2_opt1, p1_opt1 = max_scores(i+1, j)

            p2_opt2, p1_opt2 = max_scores(i, j-1)

            if p2_opt1 < p2_opt2:
                return p1_opt1 + nums[i], p2_opt1
            else:
                return p1_opt2 + nums[j], p2_opt2

        p1, p2 = max_scores(0, N-1)

        return p1 >= p2