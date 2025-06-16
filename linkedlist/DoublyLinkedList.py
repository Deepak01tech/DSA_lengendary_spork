class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        #we are creating DoublyLinked List
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insertBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        if self.head is not None:
            self.head.prev=newNode
        self.head=newNode

    def insertAtIndex(self,data,index):
        if index==0:
            self.insertBegin(data)
            return
        pos=0
        curr=self.head

        while curr is not None and pos+1!=index:
            pos+=1
            curr=curr.next
        if curr is not None:
            newNode=Node(data)
            newNode.next=curr.next
            newNode.prev=curr
            if curr is not None:
                curr.next.prev=newNode
            curr.next=newNode
        else:
            print("Sorry no such index")


    def insertEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newNode
        newNode.prev=curr


    def updateNode(self,val,index):
        cur=self.head
        pos=0
        while cur is not None and pos!=index:
            pos+=1
            cur=cur.next
        if cur is not None:
            cur.data=val
        else:
            print("NO such index found in the linkedList")

    def deleteAtIndex(self,index):
        if self.head is None:
            return
        if index==0:
            if self.head.next is not None:
                self.head.next.prev=None
            self.head=self.head.next
            return
        cur=self.head
        pos=0
        while cur is  not None and pos+1!=index:
            pos+=1
            cur=cur.next
        if cur is None:
            print("NO such index found in the linkedList")
            return
        if cur.next is not None:
            cur.next.prev=cur.prev
        if cur.prev is not None:
            cur.prev.next=cur.next


    def printForward(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next


    def printBackward(self):
        cur = self.head
        while cur.next is not None:
            # print(cur.data)
            cur = cur.next
        tail=cur

        while tail:
            print(tail.data)
            tail=tail.prev



l1=DoublyLinkedList()
l1.insertBegin(1)
l1.insertBegin(2)
l1.insertBegin(3)
l1.insertBegin(4)
print("Left to right")
l1.printForward()
print("Right to left")
l1.printBackward()
print("-"*10)
l1.insertAtIndex(99,0)
l1.printForward()
print("-"*10)
l1.deleteAtIndex(10)
print("-"*10)
l1.printForward()
print("-"*10)
l1.updateNode(79,0)
l1.printForward()
print("-"*10)
l1.insertEnd(100)
l1.printForward()
l1.insertAtIndex(99999,99)
print("-"*10)
l1.printForward()

