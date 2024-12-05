class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')

        for c in path:
            if c == "." or c == "":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return '/' + '/'.join(stack)