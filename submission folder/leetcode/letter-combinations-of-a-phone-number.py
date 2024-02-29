class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = { "2": list("abc"), 
                    "3": list("def"), 
                    "4": list("ghi"), 
                    "5": list("jkl"), 
                    "6": list("mno"), 
                    "7": list("pqrs"), 
                    "8": list("tuv"), 
                    "9": list("wxyz")
                    }
        res = []
        curr = []
        def backtrack(start):
            if start == len(digits):
                res.append(''.join(curr))
            else:
                for letter in keyboard[digits[start]]:
                    curr.append(letter)
                    backtrack(start+1)
                    curr.pop()

        if not digits:
            return []

        backtrack(0)
        return res



        

