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

def inorder(root):
    if root!= None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
