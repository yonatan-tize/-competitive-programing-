class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = []
        
        while x > 0:
            ans.append(x % 10)
            x //= 10
        l, r = 0, len(ans)-1
        while l < r:
            if ans[l] != ans[r]:
                return False
            l += 1
            r -= 1
        return True
        