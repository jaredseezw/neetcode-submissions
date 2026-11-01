# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def adder(l1, l2, carry) -> Optional[ListNode]:
            if not l1 and not l2:
                return ListNode(carry) if carry else None
            
            if l1 and l2:
                total = l1.val + l2.val + carry
                next1, next2 = l1.next, l2.next
            elif l1:
                total = l1.val + carry
                next1, next2 = l1.next, None
            else:
                total = l2.val + carry
                next1, next2 = None, l2.next
            
            return ListNode(total, adder(next1, next2, 0)) if total < 10 else ListNode(total - 10, adder(next1, next2, 1))

        return adder(l1, l2, 0)