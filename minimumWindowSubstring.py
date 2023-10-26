class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        minimum = len(s)+1
        counter_t = Counter(t)
        counter_search = defaultdict(int)
        count = 0
        minimum_window = ""

        for right in range(len(s)):
            counter_search[s[right]] += 1
            if s[right] in counter_t: 
                if counter_search[s[right]] <= counter_t[s[right]]:
                    count += 1
            
            while left <= right and count == len(t):
                if minimum > right - left + 1:
                    minimum = right - left + 1
                    minimum_window = s[left : right + 1]
                
                counter_search[s[left]] -= 1
                if s[left] in counter_t and counter_search[s[left]] < counter_t[s[left]]:
                    count-=1
                    
                left += 1
            
        return minimum_window
