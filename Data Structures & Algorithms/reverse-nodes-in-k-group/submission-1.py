# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        traversal = head
        #Obtain the length 
        while traversal:
            length += 1
            traversal = traversal.next

        times = length // k #no. of list to be reversed
        traversal = head

        i = 0
        dummy = ListNode(0, head)  # Added
        before = dummy            # Added
        
        while i < times:
            count = 0
            #reverse the first k
            prev = None
            original_Node = traversal
            while count < k:
                next1 = traversal.next
                traversal.next = prev
                prev = traversal 
                traversal = next1
                count += 1
            original_Node.next = traversal
            before.next = prev       # Added: connect to new group head
            before = original_Node   # Added: advance to new group tail
            i += 1

        return dummy.next

