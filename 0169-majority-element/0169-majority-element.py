class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj, count = 0, 0
        for num in nums:
            if count == 0:
                maj = num
            count += (1 if num == maj else -1)
        return maj

        # n =  len(nums)
        # count = collections.Counter(nums)
        # for num in nums:
        #     if count[num] > (n / 2):
        #         return num