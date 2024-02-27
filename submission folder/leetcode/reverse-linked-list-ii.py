# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            tail = curr

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return (prev, tail)


        # if left == right:
        #     return head

        dummy = ListNode()
        dummy.next = head
        head = dummy
        temp = dummy
        prev = dummy
        for i in range(right):
            temp = temp.next
            if temp:
                prev = temp.next
            else:
                prev = temp
        temp.next = None 

        curr = head 
        for i in range(left-1):
            curr = curr.next
        p = curr.next
        curr.next = None 

        curr_head, tail = reverse(p)
        curr.next = curr_head
        if tail:
            tail.next = prev
 
        return head.next

                