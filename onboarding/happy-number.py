class Solution:
    def isHappy(self, n: int) -> bool:
        a = set()
        a.add(n)
        while True:
            total = 0
            while n > 0:
                s = n % 10
                print(s)
                n //= 10
                total += s**2
                print(total)
            if total == 1:
                return True
            elif total in a:
                return False
            a.add(total)
            n = total
        return False


        