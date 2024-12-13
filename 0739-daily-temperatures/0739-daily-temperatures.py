class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create a hashmap to store next greater number for each number
        #crete a stack to keep track of the numbers whose next greater number is not found yet
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevIdx = stack.pop()
                result[prevIdx] = i - prevIdx
            stack.append(i)
        
        return result

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break
        # return result