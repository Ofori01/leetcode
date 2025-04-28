class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None





class MyLinkedList:

    def __init__(self):
        # list always knows the head and size
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        # always use the head. Since the list always knows the head it's better to iterate this way set a element to it and keep going to cur.next
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        # get head create new node and set next to current head.Note this is not padded head
        # new = ListNode(val)
        # new.next = self.head
        # self.head = new   
        # self.size+=1     
            # or just reuse methods
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        # get list tail and set tail.head to new node 
        # cur= self.head
        # for _ in range(size-1):
        #     cur = cur.next
        # tail = ListNode(val)
        # cur.next = tail
        # self.size+=1   
            # or just reuse methods
        self.addAtIndex(self.size,val)



        

    def addAtIndex(self, index: int, val: int) -> None:
        # check bounds first using size that the class always knows
        if index >self.size:
            return
        # for heads
        if index <= 0:
            new  = ListNode(val)
            new.next = self.head
            self.head = new
        
        else:
            cur  = self.head
            for _ in range(index-1):
                cur = cur.next
            new  = ListNode(val)
            new.next = cur.next
            cur.next = new
        self.size+=1

        # make prev ...before index.point to new node and new node point to prev.nex
        

    def deleteAtIndex(self, index: int) -> None:
        # check bounds before 

        if index < 0 or index >=self.size:
            return

        cur  = self.head
        if index ==0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
        self.size-=1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)