class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x  = 1/x 
            n = -n

        curr = self.myPow(x, n // 2) 
        if n % 2 == 0:
            return (curr * curr) 
        
        return x * (curr * curr) 

 

        

        
