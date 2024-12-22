class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #create a dict to match an opening to closing tag
        #create a stack to hold the values of the opening tag
        #iterate therough the string and add to stack if the parentehese is opening
        #and remove from the stack the opening parenthese when you encounter the closing parenthese
        #return true if the stack is empty
        matches = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in matches.values():
                stack.append(c)
            elif c in matches.keys():
                if stack and matches[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack
            