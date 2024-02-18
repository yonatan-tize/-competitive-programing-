class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {')':'(', ']':'[', '}': '{'}
        for char in s:
            if char not in store:
                stack.append(char)
            else:
                if stack and stack[-1] == store[char]:
                    stack.pop()
                else:
                    return False
            

        return len(stack) == 0 