class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                temp = 0
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                stack.append(max(1, 2 * temp))
        return sum(stack)