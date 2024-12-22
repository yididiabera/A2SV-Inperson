class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        #create a stack
        #iterate over the string and if the char is not string append it to 
        #the stack, otherwise pop from the stack
        stack = []
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)