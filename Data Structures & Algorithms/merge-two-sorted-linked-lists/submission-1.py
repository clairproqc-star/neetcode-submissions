# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        other = None
        
        if list1 and ((list2 and list1.val<=list2.val) or list2 is None):
            dummy.next=list1
            other= list2
        else:
            dummy.next=list2
            other=list1
        curr = dummy.next
        while curr:
            nxt=curr.next
            if other is None:
                return dummy.next
            
            if (nxt and nxt.val>other.val) or nxt is None:
                curr.next = other
                other = nxt
            curr = curr.next
        return dummy.next
        