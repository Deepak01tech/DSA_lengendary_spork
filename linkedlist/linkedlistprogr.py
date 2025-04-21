class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def insertinbegging(head,data):
        temp=Node(data)
        temp.next=head
        return temp


    def printlist(head):
        curr=head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next

if __name__ == "__main__":
    head = None
    head = linkedlist.insertinbegging(head, 10)
    head = linkedlist.insertinbegging(head, 20)
    head = linkedlist.insertinbegging(head, 30)

    linkedlist.printlist(head)


