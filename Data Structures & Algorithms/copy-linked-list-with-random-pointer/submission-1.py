"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashtable = {None : None}
        traversal = head
        
        #Copy nodes into hashtable
        while traversal:
            hashtable[traversal] =  Node(traversal.val)
            traversal = traversal.next
        
        #Copy the next
        traversal2 = head
        while traversal2:
            hashtable[traversal2].next = hashtable[traversal2.next]
            hashtable[traversal2].random = hashtable[traversal2.random]
            traversal2 = traversal2.next
        return hashtable[head]


        
