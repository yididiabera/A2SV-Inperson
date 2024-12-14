class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 *n):
            curNum = nums[i % n]

            while stack and curNum > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = curNum
            if i < n:
                stack.append(i)
        return result

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[j] > nums[i]:
        #             result[i] = nums[j]
        #             break
        # return result