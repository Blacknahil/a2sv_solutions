class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.dummy=Node(0)
        self.size=0
    def get(self, index: int) -> int:
        if index>self.size or index<0:
            return -1
        cur=self.dummy.next
        i=0
        while cur and i!=index:
            cur=cur.next
            i+=1
        if cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node=Node(val)
        if not self.dummy.next:
            self.dummy.next=node
        else:
            head=self.dummy.next
            self.dummy.next=node
            node.next=head
        self.size+=1
        # print(self.dummy.next.val)

    def addAtTail(self, val: int) -> None:
        node=Node(val)
        prev=self.dummy
        cur=prev.next
        while cur:
            prev=cur
            cur=cur.next
        # print(prev.val)
        prev.next=node
        self.size+=1
        # print(prev.next.val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size or index<0:
            return
        prev=self.dummy
        cur=prev.next
        # print(cur.val)
        for _ in range(index):
            prev=cur
            cur=cur.next
        # print(cur.val)
        # print(prev.val)
        node=Node(val)
        prev.next=node
        if cur:
            node.next=cur
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return 
        prev=self.dummy
        cur=prev.next
        for _ in range(index):
            prev=cur
            cur=cur.next
        prev.next=cur.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)