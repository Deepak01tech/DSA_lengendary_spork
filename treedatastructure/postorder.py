class Node:
    def __init__(self,k):
        self.key=k
        self.right=None
        self.left=None

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

def postorder(root):
    if root!= None:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")



