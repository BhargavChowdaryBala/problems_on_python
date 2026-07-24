class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Bst:
    def __init__(self,root=None):
        self.root=root
        self.l=[]

    def insert(self,root,x):
        if root is None:
            return Node(x)

        if x < root.data:
            root.left=self.insert(root.left,x)
        elif x > root.data:
            root.right=self.insert(root.right,x)

        return root

    def traversal(self,root):
        if root:
            self.traversal(root.left)
            print(root.data,end=" ")
            self.traversal(root.right)

    def inorderList(self,root):
        if root:
            self.inorderList(root.left)
            self.l.append(root.data)
            self.inorderList(root.right)

    def commonElements(self,bst2):
        self.l=[]
        bst2.l=[]

        self.inorderList(self.root)
        bst2.inorderList(bst2.root)

        i=0
        j=0

        print("Common Elements:")

        while i<len(self.l) and j<len(bst2.l):

            if self.l[i]==bst2.l[j]:
                print(self.l[i],end=" ")
                i+=1
                j+=1

            elif self.l[i] < bst2.l[j]:
                i+=1

            else:
                j+=1


# First BST
obj1=Bst()

l1=list(map(int,input("Enter BST1 elements: ").split()))

for x in l1:
    obj1.root=obj1.insert(obj1.root,x)

# Second BST
obj2=Bst()

l2=list(map(int,input("Enter BST2 elements: ").split()))

for x in l2:
    obj2.root=obj2.insert(obj2.root,x)

print("BST1:")
obj1.traversal(obj1.root)

print("\nBST2:")
obj2.traversal(obj2.root)

print()
obj1.commonElements(obj2)




