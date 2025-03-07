class Solution:
    def SieveOfEratosthenes(self, left, right):
        if left < 2:
            left = 2

        prime = [True for i in range(right+1)]
        p = 2

        while p * p <= right:
            if prime[p]:
                for i in range(p * p, right+1, p):
                    prime[i] = False
            p += 1

        return [p for p in range(left, right + 1) if prime[p]]

    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = self.SieveOfEratosthenes(left, right)

        if len(res) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        pair = (-1, -1)

        for i in range(1, len(res)):
            curr_diff = res[i] - res[i - 1]
            
            if curr_diff < min_diff:
                min_diff = curr_diff
                pair = (res[i - 1], res[i])
        
        return pair
