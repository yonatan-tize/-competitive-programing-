class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for char in s:
            if char.isalnum():
                a += char.lower()
        l, r = 0, len(a)-1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True
