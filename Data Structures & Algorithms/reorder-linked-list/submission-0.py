# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = middle = head
        if not head:
            return

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        second = middle.next
        middle.next = None
        prev = None
        next1 = second
        #Reverse second
        while second:
            next1 = second.next 
            second.next = prev
            prev = second 
            second = next1
        second = prev

        while second:
            next_first = head.next
            next_second = second.next

            head.next = second
            second.next = next_first

            head = next_first
            second = next_second