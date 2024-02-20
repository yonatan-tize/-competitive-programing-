# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2, dummy, temp):
            if not list1 or not list2:
                temp.next = list1 or list2
                return dummy.next

            if list1.val <= list2.val:
                temp.next = list1
                return merge(list1.next, list2, dummy, temp.next)

            else:
                temp.next = list2
                return merge(list1, list2.next, dummy, temp.next)

            return dummy.next

        dummy = ListNode()
        temp = dummy

        return merge(list1, list2, dummy, temp)
