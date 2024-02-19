# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greaterDummy = ListNode()
        smallerDummy = ListNode()
        d1 = greaterDummy
        d2 = smallerDummy
        temp = head

        while temp:
            if temp.val >= x:
                node = ListNode(temp.val)
                d1.next = node
                d1 = d1.next
            else:
                node = ListNode(temp.val)
                d2.next = node
                d2 = d2.next

            temp = temp.next

        d2.next = greaterDummy.next

        return smallerDummy.next

