# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow =slow.next
    
        prev, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True    
        
        # nums = []
        # temp = head
        # while temp:
        #     nums.append(temp.val)
        #     temp = temp.next
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True