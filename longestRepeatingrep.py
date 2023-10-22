class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        ans = 0
        max_freq = 0
        a = {}

        while right < len(s):
            a[s[right]] = a.get(s[right], 0) + 1
            max_freq = max(max_freq, a[s[right]])
            ws = right - left + 1
            if ws - max_freq <= k:
                ans = max(ans, ws)
                
            else:
                while ws - max_freq > k:
                    a[s[left]] -= 1
                    left += 1
                    ws = right - left + 1
            right += 1
        return ans