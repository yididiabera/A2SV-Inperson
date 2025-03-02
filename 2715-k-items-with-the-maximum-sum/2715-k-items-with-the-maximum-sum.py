class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        bag = []
        for _ in range(numOnes):
            bag.append(1)
        for _ in range(numZeros):
            bag.append(0)
        for _ in range(numNegOnes):
            bag.append(-1)
        bag.sort(reverse=True)
        return sum(bag[:k])