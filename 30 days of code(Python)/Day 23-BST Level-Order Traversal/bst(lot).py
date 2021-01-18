import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def height(self,root):
        if(root==None):
            return 0
        else:
            lheight=self.height(root.left)
            rheight=self.height(root.right)
            if(lheight>rheight):
                return lheight+1
            else:
                return rheight+1
    def printElements(self,root,level):
        if(root==None):
            return 0
        if(level==1):
            print(root.data,end=" ")
        else:
            self.printElements(root.left,level-1)
            self.printElements(root.right,level-1)
          
              

    def levelOrder(self,root):
        #Write your code here
        h = self.height(root)
        for i in range(1,h+1):
            self.printElements(root,i)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
