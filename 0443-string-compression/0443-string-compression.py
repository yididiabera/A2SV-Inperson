class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, j = 0, 0

        while i < len(chars):
            cur_char = chars[i]
            count = 0

            while i < len(chars) and cur_char == chars[i]:
                count += 1
                i += 1
            
            chars[j] = cur_char
            j += 1

            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            
        return j