#Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.class Node(object):    def __init__(self,value):        self.value = value        self.nextnode = Nonedef reverse(head):    currentnode=head    prev_node=None    nex_node=None    while currentnode:        nex_node=currentnode.nextnode        currentnode.nextnode=prev_node        prev_node=currentnode        currentnode=nex_node    return prev_node# Create a list of 4 nodesa = Node(1)b = Node(2)c = Node(3)d = Node(4)# Set up order a,b,c,d with values 1,2,3,4a.nextnode = bb.nextnode = cc.nextnode = dprint a.nextnode.valueprint b.nextnode.valueprint c.nextnode.valueprint reverse(a)