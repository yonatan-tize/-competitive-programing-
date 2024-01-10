class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        count_black = 0
        right = k-1
        for i in range(k-1):
            if blocks[i] == 'B':
                count_black += 1

        min_operation = k
        for right in range(k-1, len(blocks)):
            if blocks[right] == 'B':
                count_black += 1
            min_operation = min(min_operation, k-count_black)
            if blocks[left] == 'B':
                count_black -= 1
            left += 1

        return min_operation