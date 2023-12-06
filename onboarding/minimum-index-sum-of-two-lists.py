class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        store = {}
        ans = []
        index = len(list1) + len(list2)
        for i, word1 in enumerate(list1):
            for j, word2 in enumerate(list2):
                if word1 == word2:
                    store[word1] = i+j
                    index = min(i+j, index)
                    break
        
        for key, value in store.items():
            if value == index:
                ans.append(key)
        return ans

