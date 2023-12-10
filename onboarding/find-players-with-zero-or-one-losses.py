class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = defaultdict()
        for winner, loser in matches:
            if loser not in count or count[loser] > 0:
                count[loser] = -1
            elif loser in count:
                count[loser] -= 1
            if winner not in count:
                count[winner] = 1
            elif winner in count and count[winner] <= -1:
                continue
            else:
                count[winner] += 1 
        winners = []
        losers = []
        for key, value in count.items():
            if value > 0:
                winners.append(key)
            elif value == -1:
                losers.append(key)
        winners.sort()
        losers.sort()
        return [winners, losers ]

