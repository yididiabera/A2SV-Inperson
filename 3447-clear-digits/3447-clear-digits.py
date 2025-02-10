class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if '0' <= c <= '9' and stack:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        return "".join(stack)
