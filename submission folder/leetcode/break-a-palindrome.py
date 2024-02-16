class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size = len(palindrome)
        if size == 1:
            return ''

        ans = ''
        right = 0

        while right < len(palindrome):
            if palindrome[right] != 'a' and right != size // 2:
                ans = palindrome[:right] +  'a' + palindrome[right+1:]
                return ans
            right += 1

        ans = palindrome[:size-1] + 'b'
        return ans



