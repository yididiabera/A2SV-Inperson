class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_count = 0
        balance = 0

        for ch in s:
            if ch == 'R':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                balanced_count += 1
        
        return balanced_count