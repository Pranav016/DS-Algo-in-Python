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
        y=self.r.get()
        while not self.r.empty():
            x=self.r.get()
            self.s.put(x)
        self.s,self.r=self.r,self.s
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
        self.r,self.s=self.s,self.r
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
