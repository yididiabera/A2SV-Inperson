from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars * cars  # Binary search range

        def can_repair_in_time(t):
            total_cars = sum(int(math.sqrt(t // r)) for r in ranks)
            return total_cars >= cars

        while left < right:
            mid = (left + right) // 2
            if can_repair_in_time(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time

        return left
