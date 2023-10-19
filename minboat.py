class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                count += 1
                l += 1 
            elif people[l] + people[r] >= limit:
                count += 1
            r -= 1
        return count