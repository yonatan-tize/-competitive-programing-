class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_len = 0
        vowel_dict = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        count = 0
        for i in range(k-1):
            if s[i] in vowel_dict:
                count += 1

        for j in range(k-1, len(s)):
            if s[j] in vowel_dict:
                count += 1
            max_len = max(max_len, count)
            
            if s[left] in vowel_dict:
                count -= 1
            left += 1 
        return max_len