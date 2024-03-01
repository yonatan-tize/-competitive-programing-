class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s, open, close):
            if open == 0 and close == 0:
                ans.append(s)
                return 

            if open == close:
                s += '('
                backtrack(s, open-1, close)
                # s = s[:-1]


            elif open < close and open > 0:
                s += '('
                backtrack(s, open-1, close)
                s = s[:-1]
                s += ')'
                backtrack(s, open, close-1)

            elif open == 0 and close:
                s += ')'
                backtrack(s, open, close-1)

        backtrack('', n, n)

        return ans
          
