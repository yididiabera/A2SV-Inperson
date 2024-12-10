class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefixSum.append(total)



    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            _sum = self.prefixSum[right] - self.prefixSum[left -1]
            return _sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums
# param_1 = obj.sumRange(left,right)