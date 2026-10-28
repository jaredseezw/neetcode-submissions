# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        hashtable = {}
        
        while head:
            if head.val in hashtable and hashtable[head.val] < index:
                return True
            else:
                hashtable[head.val] = index
                index += 1
                head = head.next
        return False