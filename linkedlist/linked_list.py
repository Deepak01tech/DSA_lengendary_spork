class Node():
    def __init__(self,data):
        self.data = data
        self.next= Node
class Linked_list():
    def __init__(self):
        self.head=None
    def print_list(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next

        





