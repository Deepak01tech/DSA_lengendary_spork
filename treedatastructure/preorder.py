class Node:
    def __init__(self,k):
        self.key=k
        self.right=None
        self.left=None

def preorder(root):
    if root!= None:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)