# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        big = ListNode()
        small_head = small
        big_head = big
        temp = head
        
        while temp:
            if temp.val < x:
                small.next = temp
                small = small.next
            else:
                big.next  = temp
                big = big.next
            temp = temp.next
        
        small.next = big_head.next
        big.next = None
        return small_head.next