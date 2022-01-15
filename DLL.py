#Creating Node
from lib2to3.pytree import Node


class NODE():
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        self.prevval=None
# creating DLL class
class DLL():
    def __init__(self):
        self.headval=None
# Inserting elements at Beginning
    def insertBegin(self,newval):
        NewNode=NODE(newval)
        NewNode.nextval=self.headval
        self.headval=NewNode
# Traversing DLL elements
    def TraverseList(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
# Inserting elements at End
    def insertEnd(self,newval):
        NewNode=NODE(newval)
        if self.headval is None:
            self.headval=NewNode
            return
        tmp=self.headval
        while(tmp.nextval):
            tmp=tmp.nextval
        tmp.nextval=NewNode
L=DLL()
L.headval=NODE(77)
L.insertBegin(7)
L.insertEnd(777)
L.TraverseList()