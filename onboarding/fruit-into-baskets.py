class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        store = defaultdict(int)
        left = 0
        max_fruit = 0
        for right in range(len(fruits)):
            store[fruits[right]] = right 
            if len(store) > 2:
                left = min(store.values()) 
                del store[fruits[left]]
                left += 1
            max_fruit = max(max_fruit, right-left+1)

        return max_fruit
