
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)  # 哨兵节点，方便操作
        self.tail = self.head
    
    def get(self, index: int) -> int:
       cur = self.head.next
       for _ in range(index):
           if cur is None:
               return -1
           cur = cur.next
       return cur.val if cur else -1 
    def insertHead(self, val: int) -> None:
        if self.head.next is None:
            self.tail = ListNode(val)
            self.head.next = self.tail
        else:
            self.head.next = ListNode(val, self.head.next)

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        for _ in range(index):
             if cur.next:
                cur = cur.next 
            
        if cur.next is None:
            return False  
        if self.tail == cur.next:
            self.tail = cur
        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        cur = self.head.next
        res=[]
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
