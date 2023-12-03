class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def stringToInt(num):
            n = 0
            for i in range(len(num)):
                c = num[i]
                n = n * 10 + int(c)
            return n
        num1 = stringToInt(num1)
        num2 = stringToInt(num2)
        return str(num1*num2)


