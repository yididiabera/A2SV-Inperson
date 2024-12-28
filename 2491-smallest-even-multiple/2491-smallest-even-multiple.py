class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return 2 * n
        # def GCD(dividend, divisor):
        #     while divisor != 0:
        #         dividend, divisor = divisor, dividend % divisor
        #     return dividend
        # dividend = max(2, n)
        # divisor = min(2, n)
        # result = (dividend * divisor) // GCD(dividend, divisor)
        # return result
