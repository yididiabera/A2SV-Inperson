class Solution:
    def decodeString(self, s: str) -> str:
        # 3 [ a 2 [ c ] ]
        # 0 1 2 3 4 5 6 7

        close = [0] * len(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(i)
            elif s[i] == ']':
                close[stack.pop()] = i
        
        def decode(i, j):
            nonlocal s
            nonlocal close
            num = ''
            ans = ''

            while i < j:
                if s[i].isdigit():
                    num += s[i]
                    #i += 1
                
                elif s[i].isalpha():
                    ans += s[i]
                    #i += 1
                
                else:
                    ans += int(num) * decode(i + 1, close[i])
                    i = close[i]
                    num  = ""
                
                i += 1
            return ans
        return decode(0, len(s))