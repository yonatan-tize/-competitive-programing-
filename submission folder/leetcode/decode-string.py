class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''

        for i, char in enumerate(s):
            if char == ']':
                a = ''
                c = ''
                while stack[-1].isalpha():
                    c = stack.pop() + c

                stack.pop()
                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                if n.isdigit():
                    a = c * int(n)
                else:
                    a = c
                
                stack.append(a)

            else:
                stack.append(char)

        return ''.join(stack)
    



