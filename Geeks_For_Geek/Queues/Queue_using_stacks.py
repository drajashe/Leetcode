#creating a queue using 2 stacks

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def deQueue(self):

        if(len(self.s1)==0 and len(self.s2)==0):
            print("Queue empty")
            return

        if(len(self.s2)==0):
            while(len(self.s1)):
                #print(self.s1[-1])
                self.s2.append(self.s1[-1])
                self.s1.pop()
            #print(self.s2[0])
        x=self.s2[0]
        self.s2.pop()
        return (x)
    def enQueue(self,x):
        self.s1.append(x)

        print(self.s1)

        return self.s1


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.deQueue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    print(q.deQueue())
    q.enQueue(1)
    q.enQueue(2)
    print(q.deQueue())
    print(q.deQueue())





