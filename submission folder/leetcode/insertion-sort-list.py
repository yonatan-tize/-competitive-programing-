# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, head1, head2):   # to merge the two linkedlist
        dummy = ListNode()
        temp = dummy

        while head1 and head2:
            if head1.val < head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next

        temp.next = head1 or head2
        return dummy.next

    def midNode(self, head): # a function to find the midlle linkedlist
        slow = head
        fast = head
        prev = head

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
       
        prev.next = None

        return slow  
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.midNode(head)
        left = self.insertionSortList(head)
        right = self.insertionSortList(mid)

        return self.mergeList(left, right)