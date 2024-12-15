class Solution:
    def pivotInteger(self, n: int) -> int:
        rightSum = 0
        leftSum = 0
        for i in range(1, n + 1):
            rightSum += i

        for i in range(1, n + 1):
            leftSum += i
            if leftSum == rightSum:
                return i
            rightSum -= i
        return -1