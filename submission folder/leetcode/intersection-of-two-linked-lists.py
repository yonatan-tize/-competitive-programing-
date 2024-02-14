# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        countA = 0
        countB = 0
        tempA = headA
        tempB = headB

        while tempA:
            countA += 1
            tempA = tempA.next
        
        while tempB:
            countB += 1
            tempB = tempB.next

        tempA = headA
        tempB = headB
        if countA > countB:
            while countA > countB:
                tempA = tempA.next
                countA -= 1
        if countA < countB:
            while countA < countB:
                tempB = tempB.next
                countB -= 1

        while tempA and tempB:
            if tempA == tempB:
                return tempA

            tempA = tempA.next
            tempB = tempB.next 

        return None


