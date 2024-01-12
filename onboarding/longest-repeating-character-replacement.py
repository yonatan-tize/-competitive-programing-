class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = defaultdict(int)
        left = 0
        answer = 0
        max_freq = 0
        for right in range(len(s)):
            store[s[right]] += 1  
            max_freq = max(max_freq, store[s[right]])
            ws = right-left + 1
            while ws - max_freq > k:
                store[s[left]] -= 1  
                left += 1
                ws = right-left+1
            answer = max(answer, ws)

        return answer
