class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None



    def print_llist(self):
        temp =llist.head
        while(temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;  # Link first node with second
    second.next = third;  # Link second node with the third node

    llist.print_llist()

