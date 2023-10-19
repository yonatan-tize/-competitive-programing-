class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i1, i2 = 0, 0
        count = 0

        while i1 < len(players) and i2 < len(trainers):
            if players[i1] <= trainers[i2]:
                count += 1
                i1 += 1
            i2 += 1

        return count
