class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Bst:
    def __init__(self,root=None):
        self.root=root
        self.c=0
        self.l=[]
        self.b=False
        self.l1=[]
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
    
    def  sumEqualToTarget(self,target):
        if(self.root==None):
            return 
        q=[self.root]
        while q:
            node=q.pop(0)
            
            if(target-node.data in l):
                self.l1.append(node.data)
                self.l1.append(target-node.data)
                self.b=True
                break
            l.append(node.data)
            if(node.left!=None):
                q.append(node.left)
            if(node.right!=None):
                q.append(node.right)


        
        
               

                
            




obj=Bst(None)

l=list(map(int,input().split()))
for i in l:
    obj.root=obj.insert(obj.root,i)
print("elments inserted are:")
obj.traversal(obj.root)
print()
n=int(input("Enter target"))
obj.sumEqualToTarget(n)
if(obj.b):
    print("pair present")
    print("Pair is")
    print(obj.l1)
else:
    print("No pair present")


