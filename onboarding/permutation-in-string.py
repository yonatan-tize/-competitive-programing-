class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count_s1 = Counter(s1)
        window_size = len(s1)
        count_s2 = defaultdict(int)

        for i in range(window_size-1):
            count_s2[s2[i]] += 1 
        
        left = 0
        for j in range(window_size-1, len(s2)):
            count_s2[s2[j]] += 1 
            if count_s2 == count_s1:
                return True

            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]
            left += 1
        
        return False
            