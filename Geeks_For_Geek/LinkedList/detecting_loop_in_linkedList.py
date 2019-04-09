class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None

    def print_LinkedList(self):
        current=self.head;
        while(current ):
            print(current.data)
            current=current.next
    def detect_loop(self):
        take_set = set()
        head_ = current = self.head

        while(current is not None):
            if(current not in take_set):
                take_set.add(current)
            elif(current in take_set):
                return True
            current = current.next
            #print(temp.data)

        return False


if __name__ == '__main__':
    lList= LinkedList()


    lList.head=Node(8)
    second = Node(7)
    lList.head.next=second
    third=Node(8)
    second.next=third
    lList.head.next.next.next= lList.head

    check_if_loop = lList.detect_loop()
    lList.print_LinkedList()
    if(lList.detect_loop()):
        print("present")
    else:
        print("not present")








