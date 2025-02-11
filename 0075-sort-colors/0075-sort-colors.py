class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, p0, p2 = 0, 0, len(nums) - 1

        while p <= p2:
            if nums[p] == 0:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
                p += 1
            elif nums[p] == 2:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1

        # count = Counter(nums) # O(3)
        # idx = 0
        # print(count)

        # for color in range(3):
        #     for _ in range(count[color]):
        #         nums[idx] = color
        #         idx += 1
        # print(count[9])
        # count = Counter(nums)
        # result = []

        # count_sorted = dict(sorted(count.items(), key=lambda item : item[1]))

        # for key, value in count_sorted.items():
        #     for _ in range(value):
        #         result.append(key)
        # return result
