# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeSortedLists(self, list1, list2) -> ListNode:
            ans = ListNode(0)
            traversal = ans
            while list1 and list2:
                if list1.val < list2.val:
                    traversal.next = list1
                    traversal = traversal.next
                    list1 = list1.next
                else:
                    traversal.next = list2
                    traversal = traversal.next
                    list2 = list2.next
            if list1:
                traversal.next = list1
            else:
                traversal.next = list2
            return ans.next    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Recursively merge adjacent lists
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                second = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeSortedLists(lists[i], second))
            lists = merged
        return lists[0] if lists else None
                