class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        queue = deque()
        for i, num in enumerate(tickets):
            queue.append(i)

        count = 0
        
        while tickets[k] != 0:
        
            index = queue.popleft()
            tickets[index] -= 1
            count += 1

            if index == k and tickets[k] == 0:
                return count

            if tickets[index] == 0:
                continue

            queue.append(index)
            

        return count

                
