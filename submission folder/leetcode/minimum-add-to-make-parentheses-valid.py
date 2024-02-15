class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_open = 0
        num_closed = 0

        for sign in s:
            if sign == '(':
                num_open += 1
            else:
                if sign == ')' and num_open > 0:
                    num_open -= 1
                else:
                    num_closed += 1

        return num_open + num_closed

                    


