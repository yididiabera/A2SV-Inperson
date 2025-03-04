class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills = 0
        ten_bills = 0
        twenty_bills = 0

        for bill in bills:
            if bill == 5:
                five_bills += 1
            elif bill == 10:
                ten_bills += 1
                if five_bills > 0:
                    five_bills -= 1
                else:
                    return False
            elif bill == 20:
                if ten_bills > 0 and five_bills > 0:
                    ten_bills -= 1
                    five_bills -= 1
                elif five_bills > 2:
                    five_bills -= 3
                else:
                    return False
                
        return True
                
                # if ten_bills > 0:
                #     ten_bills -= 1
                #     if five_bills > 0:
                #         five_bills -= 1
                #     else:
                #         return False
                # else:
                #     if five_bills > 2:
                #         five_bills -= 3
                #         bill -= 5
                #     else:
                #         return False
