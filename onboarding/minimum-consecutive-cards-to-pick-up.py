class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_index = defaultdict(list)
        for i, card in enumerate(cards):
            card_index[card].append(i)

        min_distance = len(cards)+1
        for index_list in card_index.values():
            length = len(index_list)
            if length >= 2:
                for i in range(1,length):
                    curr_dist = index_list[i] - index_list[i-1] + 1
                    min_distance = min(min_distance, curr_dist)
        return min_distance if min_distance < len(cards) + 1 else -1

