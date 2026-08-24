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
        if list1 is None:
            return list2
        elif list2 is None:
            return list1        
        else: 
            if list1.val<list2.val:
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
    