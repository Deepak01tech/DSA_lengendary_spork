

class Node:
    def __init__ (self, value):
        self.data=value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_begin(self, val):
        node=Node(val)
        node.next=self.head
        self.head=node

    def insert_end(self,val):
        node=Node(val)
        if self.head is None:
            self.head=node
            return
        last_node=self.head
        while last_node.next is not None:
            last_node=last_node.next
        last_node.next=node

    def insert_atloc(self, data, loc):
        if loc==0:
            self.insert_begin(data)
            return

        pos=0
        a=self.head
        while a and pos<loc-1:
            a=a.next
            pos+=1

        if a is None:
            print("Invalid")
            return

        node=Node(data)
        node.next=a.next
        a.next=node

    def delete_begin(self):
        if self.head is None:
            return
        self.head=self.head.next

    def printll(self):
        node=self.head
        while node is not None:
            print(node.data, end=" ")
            node=node.next
        print()

    def size(self):
        node=self.head
        count=0
        while node is not None:
            count+=1
            node=node.next
        # print(count)
        return count

    def empty(self):
        # if self.size()==0:
        #     return True
        # return False

        return self.head is None

l1=LinkedList()
print(l1.head)
print(l1.empty())
l1.insert_end(4)
l1.printll()
l1.insert_begin(5)
l1.printll()
l1.insert_begin(3)
l1.printll()
l1.insert_atloc(10,2)
l1.printll()
l1.insert_end(4)
l1.printll()
l1.delete_begin()
l1.printll()
l1.insert_atloc(12,3)
l1.printll()
l1.insert_begin(8)
l1.printll()
l1.insert_end(7)
l1.printll()
l1.insert_atloc(18,7)
l1.printll()
print(l1.size())
print(l1.empty())