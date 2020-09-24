class Queue:
    def __init__(self):
        self.__queue=[]
        self.__front=0
        self.__count=0
    
    def enqueue(self,data):
        self.__queue.append(data)
        self.__count+=1

    def dequeue(self):
        if self.__count==0:
            print("Queue is empty")
            return -1
        self.__front+=1
        self.__count-=1
    
    def front(self):
        if self.__count==0:
            return -1
        return self.__queue[self.__front-1]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size()==0

    def print(self):
        print(*self.__queue)


# main    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.print()
print(q.isEmpty())
print(q.size())