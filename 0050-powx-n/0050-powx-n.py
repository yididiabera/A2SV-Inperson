class Solution:
    def myPow(self, x: float, n: int) -> float:
        #base case
        if n == 0: return 1
        if x == 1: return x
        if x == 0: return 0

        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2 == 0:
            return self.myPow( x * x, n // 2)
        return x * self.myPow(x * x, n // 2)
        
