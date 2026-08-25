# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0,head)
        left=dummy
        right=head
        # move right to the right place
        while n>0:
            right=right.next
            n-=1

        # move right and left together
        while right:
            left=left.next
            right=right.next
        
        # remove the target node
        left.next=left.next.next
        return dummy.next
        


        