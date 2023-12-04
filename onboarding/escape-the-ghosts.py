class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x1, y1 = target[0], target[1]
        my_dist = abs(x1) + abs(y1)

        for x,y in ghosts:
            # d = math.sqrt((x1-x)**2 + ()**2)
            s = abs(x1-x) + abs(y1-y)
            if s <= my_dist:
                return False
        return True
