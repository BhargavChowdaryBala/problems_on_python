import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Bst:
    def __init__(self,root=None):
        self.root=root
        self.c=sys.maxsize
        self.f=-sys.maxsize-1
    def insert(self,root,x):
        if(root==None):
            return Node(x)
        elif(x<root.data):
            root.left=self.insert(root.left,x)
        elif(x>root.data):
            root.right=self.insert(root.right,x)
        else:
            print("Duplicates are not allowed")
        return root
    def traversal(self,root):
        if(root!=None):
            self.traversal(root.left)
            print(root.data, end=" ")
            self.traversal(root.right)
    def getsuccesor(self,curr):
        while(curr!=None and curr.left!=None):
            curr=curr.left
        return curr

    def delete(self,root,x):
        if(root==None):
            return root
        if(x<root.data):
            root.left=self.delete(root.left,x)
        elif(x>root.data):
            root.right=self.delete(root.right,x)
        else:
            if(root.left==None and root.right==None):
                return None
            elif(root.left==None):
                return root.right
            elif(root.right==None):
                return root.left
            else:
                s=self.getsuccesor(root.right)
                root.data=s.data
                root.right=self.delete(root.right,s.data)
        return root
    
    def floorAndceil(self, root, x):
        if root is None:
            return
        q = [root]
        while q:
            node = q.pop(0)
            if node.data >= x and node.data < self.c:
                self.c = node.data
            if node.data <= x and node.data > self.f:
                self.f = node.data
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


            
        
        
        



obj=Bst(None)

l=list(map(int,input().split()))
for i in l:
    obj.root=obj.insert(obj.root,i)
print("elments inserted are:")
obj.traversal(obj.root)
print()
n=int(input("Enter target"))
obj.floorAndceil(obj.root,n)
print("flooris",obj.f)
print("ceil",obj.c)



