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
root.right.left=Node(60)
root.right.right=Node(70)

def printnodesatkdist(root,k):
    if root==None:
        return
    if k==0:
        print(root.key,end=" ")
    else:
        printnodesatkdist(root.left,k-1)
        printnodesatkdist(root.right,k-1)
