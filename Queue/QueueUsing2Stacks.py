import queue

class  q2s:
    
    def __init__(self):
        self.r=queue.LifoQueue()
        self.s=queue.LifoQueue()
        self.count=0

    def enqueue(self,data):
        self.r.put(data)
        self.count+=1

    def dequeue(self):
        if self.r.empty():
            return -1
        while not self.r.empty():
            x=self.r.get()
            self.s.put(x)
        y=self.s.get()
        while not self.s.empty():
            x=self.s.get()
            self.r.put(x)
        self.count-=1
        return y

    def size(self):
        return self.count

    def front(self):
        if self.r.empty():
            return -1
        while not self.r.empty():
            x=self.r.get()
            self.s.put(x)
        while not self.s.empty():
            y=self.s.get()
            self.r.put(y)
            return x
        
    def isEmpty(self):
        return self.size()==0


q=q2s()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
while not q.isEmpty():
    print("front- ",q.front())
    print(q.dequeue())
