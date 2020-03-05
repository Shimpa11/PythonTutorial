"""
Tree Data Structure: BST
https://www.cs.usfca.edu/~galles/visualization/BST.html
"""

class Product:
    def __init__(self,pid,name,price,quantity=1):
        self.pid=pid
        self.name=name
        self.price=price
        self.qunatity=quantity
    def showProductDetails(self):
        print("{}|{}|{}|".format(self.pid,self.name,self.price))

class TreeNode:
    def __init__(self):
        print("TreeNode Created")
        self.object=None
        self.left=None
        self.right=None

    def showTreeNode(self):
        self.object.showProductDetails()
        print("LEFT: ",self.left,"RIGHT: ",self.right)
