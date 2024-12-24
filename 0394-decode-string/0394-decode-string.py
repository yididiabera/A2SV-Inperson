class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * subStr)
        
        return "".join(stack)