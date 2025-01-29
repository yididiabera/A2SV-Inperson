class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #result *= 10
        #result += 10
        # 121 0
        # 121 % 10 => 1  --- 121 // 10 => 12
        # 12 % 10 => 2 --- 12 // 10 => 1
        # 1 % 10 => 1 --- 1 // 10 => 0
        while x < 0:
            return False
        
        result = 0
        temp = x
        while x > 0:
            result = (result * 10) + x % 10
            x = x // 10
        
        return result == temp
    


