class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()

        while deck:
            if not queue:
                queue.append(deck.pop())

            else:
                num = queue.pop() 
                queue.appendleft(num)
                queue.appendleft(deck.pop())

        return queue

