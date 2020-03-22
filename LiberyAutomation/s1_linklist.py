class Element:
    def __init__(self, name):
        self.name = name
        self.next = None

class Linklist:
    def __init__(self):
        self.root = None
        self.len = None

    def addBegin(self, newElement):
        if self.root == None:
            self.root = newElement
        else:
            newElement.next = self.root
            self.root = newElement

    def PrintLinklist(self):
        if self.root == None:
            print("is empty")
        else:
            temp = self.root
            print(temp.name)
            while(temp.next):
                temp = temp.next
                print(temp.name)


    def RemoveElement(self, element):
        temp = self.root
        if temp.name == element:
            self.root = temp.next
        else:
            pointer = self.root
            while temp.name != element:
                pointer = temp
                temp = temp.next
            if temp.name == element:
                pointer.next = temp.next


    def addbetween(self,posion,value):
        temp = self.root
        while temp.name != posion:
            temp = temp.next
        if temp.name == posion:
            value.next = temp.next
            temp.next = value


    def addEnd(self,element):
        temp = self.root
        while (temp.next != None):
                temp = temp.next
        if temp.next == None:
            temp.next = element
l = Linklist()
elm1 = Element('a')
elm2 = Element('b')
elm3 = Element('c')

l.addBegin(elm1)
l.addBegin(elm2)
l.addBegin(elm3)
elm4 = Element('hi')

l.addEnd(elm4)
l.PrintLinklist()