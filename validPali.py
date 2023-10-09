class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        if len(s) == 1:
            return True

        while i <= j:

            while i < len(s) and s[i].isalnum() == False:
                i += 1 
            while j >= 0 and s[j].isalnum() == False:
                j -= 1 
            if i <= j:
                if s[i].lower() ==  s[j].lower():
                    i += 1
                    j -= 1 
                else:
                    return False

        return True