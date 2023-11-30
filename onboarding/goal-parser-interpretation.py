class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        l = len(command)
        i = 0
        while i < l:
            
            if command[i] == 'G':
                ans += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                ans += 'o'
                i += 2
            elif command[i] == '(' and command[i+1] == 'a':
                ans += 'al'
                i += 4
        return ans
            

