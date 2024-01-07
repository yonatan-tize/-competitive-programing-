class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        count_true = 0
        count_false = 0
        max_len = 0

        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                count_true += 1 
            else:
                count_false += 1

            while count_true > k and count_false > k:
                if answerKey[l] == 'T':
                    count_true -= 1 
                else:
                    count_false -= 1
                l += 1
            max_len = max(max_len, count_true + count_false)

        return max_len

            
             