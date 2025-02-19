# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy

        for _ in range(n):
            temp = temp.next
        aheadPtr = temp
        behindPtr = dummy
        while aheadPtr.next:
            aheadPtr, behindPtr = aheadPtr.next, behindPtr.next
        behindPtr.next = behindPtr.next.next

        return dummy.next

        # dummy = ListNode()
        # dummy.next = head
        # length = -1
        # temp = dummy
        # while temp:
        #     temp = temp.next
        #     length += 1
        # if length < 2:
        #      return None
        # temp = dummy
        # for _ in range(length - n):
        #     temp = temp.next
        # temp.next = temp.next.next

        # return dummy.next
