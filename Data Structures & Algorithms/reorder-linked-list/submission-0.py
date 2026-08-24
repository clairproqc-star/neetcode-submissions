# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # make the list into 2 parts
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        
        # reverse the second part
        curr=s.next
        s.next=None
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev

            prev=curr
            curr=nxt
        # prev is the result
        part2=prev
        
        # merge 2 parts
        part1=head
        while part1 and part2:
            tmp1, tmp2 = part1.next, part2.next
            part1.next = part2
            part2.next = tmp1
            part1, part2 = tmp1, tmp2