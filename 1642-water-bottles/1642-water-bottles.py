class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            drink = numBottles // numExchange
            result += drink
            rem = numBottles % numExchange
            numBottles = drink + rem
        return result
