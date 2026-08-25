# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        # merge every 2 nodelist into 1
        while len(lists)>1:
            mergedLists=[]
            for i in range(0, len(lists), 2):
                if i>=len(lists)-1:
                    mergedLists.append(lists[i])
                else:
                    mergedLists.append(self.mergeTwoLists(lists[i],lists[i+1]))
            lists=mergedLists
                  
        return lists[0]


    def mergeTwoLists(self,list1,list2):
        dummy=ListNode(0)
        tail=dummy
        while list1 and list2:
            if list1.val>=list2.val:
                tail.next=list2
                list2=list2.next
            else:
                tail.next=list1
                list1=list1.next
            tail=tail.next
        
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
        return dummy.next
            

