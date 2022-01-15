# Node Creating using class
class NODE():
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
#creating SLL class 
class SLL():
    def __init__(self):
        self.headval=None
    #Traversing the List 
    def traverseList(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    # Inserting list elements at beginning
    def insertBegin(self,newval):
        NewNode=NODE(newval)     
        NewNode.nextval=self.headval
        self.headval=NewNode 
    # Inserting list element at End
    def insertEnd(self,newval):
       NewNode = NODE(newval)
       if self.headval is None:
            self.headval = NewNode
            return
       tmp = self.headval
       while(tmp.nextval):
            tmp = tmp.nextval
       tmp.nextval=NewNode

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

list=SLL()
list.headval=NODE(10)
list.insertBegin(1)
list.insertEnd(20)
list.insertEnd(30)
list.insertEnd(40)
list.insertEnd(50)
list.traverseList()
list.insertPos(3,35)
print('After Inserting at Position')
list.traverseList()
