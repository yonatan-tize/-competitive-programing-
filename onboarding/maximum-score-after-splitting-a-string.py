class Solution:
    def maxScore(self, s: str) -> int:
        count_zero = 0
        count_one = s.count('1')
        max_score = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                count_zero += 1
            else:
                count_one -= 1

            total = count_one + count_zero
            max_score = max(max_score, total) 
        
        return max_score
