class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints)-k-1
        out_wSum = 0
        for i in range(right+1, len(cardPoints)):
            out_wSum += cardPoints[i]

        max_point = out_wSum
        right += 1
        while right < len(cardPoints):
            out_wSum -= cardPoints[right]
            out_wSum += cardPoints[left]
            max_point = max(out_wSum, max_point)
            right += 1
            left += 1
        
        return max_point
            
