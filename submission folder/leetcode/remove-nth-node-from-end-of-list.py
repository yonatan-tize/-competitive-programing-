# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers when one reach the end of the linked list the other will be at the desired position
        dummy = ListNode()
        dummy.next = head
        head = dummy
        slow = head
        fast = head
        count = 0

        while fast.next:
            fast = fast.next
            if count == n:
                slow = slow.next
            else:
                count += 1
                
        if n > 1: 
            slow.next = slow.next.next
        else:
            slow.next = None

        return head.next