#Creating NODE
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
# Inserting at position 
    def insertPos(self,pos,newdata):
        tmp=self.headval.nextval
        for pos in range (pos-1):
            tmp=tmp.nextval
            if tmp is None:
                print("The mentioned node is absent")
                return
        NewNode = NODE(newdata)
        NewNode.nextval = tmp.nextval
        tmp.nextval = NewNode
L=DLL()
L.headval=NODE(7)
L.insertBegin(0)
L.insertEnd(17)
L.insertEnd(27)
L.insertEnd(37)
L.TraverseList()
print('After insertion at Position')
L.insertPos(3,'Third Index')
L.TraverseList()
