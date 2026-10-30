# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        traversal = head
        while traversal:
            traversal = traversal.next
            length += 1
        #reverse the n 
        n = length - n
        if n == 0:
            return head.next
        ans = head
        while n > 1:
            head = head.next 
            n -= 1
        if head.next:
            head.next = head.next.next
        
        return ans
