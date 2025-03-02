class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        _sum = min(numOnes, k)
        k -= _sum
        
        if k > 0:
            zeros = min(numZeros, k)
            k -= zeros

        if k > 0:
            negative = min(k, numNegOnes)
            _sum -= negative
        
        return _sum