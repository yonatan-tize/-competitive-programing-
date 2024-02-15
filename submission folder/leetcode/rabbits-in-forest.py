class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        size = len(answers)
        left = 0
        right = 1
        count = 0
        
        while right <= size:

            if right == size:
                count += (1 + answers[left])
                break
            while right < size and answers[right] == answers[left] and answers[left] >= right-left :
                right += 1

            if answers[left] == 0:
                count += (right - left) 
                left = right
                right += 1
                continue
            count += 1 + answers[left]

            left = right
            right += 1

        return count 