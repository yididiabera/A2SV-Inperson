class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = 0
        nums = "".join([ str(ord(i) - 96) for i in s ])
        for _ in range(k):
            result = sum(int(i) for i in nums)
            nums = str(result)
        return result
        # nums = []
        # result = 0
        # _sum = 0 
        # for _ in range(k):
        #     for i in s:
        #         nums.append(ord(i) - 96)
        #     _sum = sum(nums)
        # return


