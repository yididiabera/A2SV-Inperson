class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {')':'(', '}': '{', ']':'['}

        for c in s:
            if c in matching.values():
                stack.append(c)
            elif c in matching.keys():
                if not stack or stack[-1] != matching[c]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
