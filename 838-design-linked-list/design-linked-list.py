class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        t=self.head
        for i in range(index):
            if not t:
                return -1
            t=t.next
        return t.val if t else -1
          
    def addAtHead(self, val: int) -> None:
        new_node=ListNode(val)
        new_node.next=self.head
        self.head=new_node
       

    def addAtTail(self, val: int) -> None:
        new_node=ListNode(val)
        if not self.head:
            self.head=new_node
            return

        t=self.head
        while t.next:
            t=t.next
        t.next=new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node=ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        t=self.head
        for i in range(index-1):
            if not t:
                return
            t=t.next
        if not t:
            return
        new_node.next=t.next
        t.next=new_node
    
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index==0:
            self.head=self.head.next
            return
        t=self.head
        for i in range(index-1):
            if not t:
                return 
            t=t.next
        if not t or not t.next:
            return
        t.next=t.next.next
       
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)