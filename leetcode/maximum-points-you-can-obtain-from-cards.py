class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints)-k-1
        out_wSum = sum(cardPoints[right+1:])
        max_point = out_wSum
        right += 1
        i = right

        for right in range(i,len(cardPoints)):
            out_wSum -= cardPoints[right]
            out_wSum += cardPoints[left]
            max_point = max(out_wSum, max_point)
            left += 1
        
        return max_point
            
