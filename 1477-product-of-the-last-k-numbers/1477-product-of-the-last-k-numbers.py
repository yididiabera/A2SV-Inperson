class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # Stores cumulative product

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # Reset when zero appears
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  # If k exceeds valid range (means zero appeared)
            return 0
        return self.prefix[-1] // self.prefix[-(k+1)]