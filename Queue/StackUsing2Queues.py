from sys import stdin
import queue

class Stack :

    def __init__(self):
        self.r=queue.Queue()
        self.s=queue.Queue()
        self.count=0

    def getSize(self):
        return self.count

    def isEmpty(self):
        return self.getSize()==0

    def push(self,data):
        self.r.put(data)
        self.count+=1

    def pop(self):
        if self.r.empty():
            return -1
        for i in range(self.count-1):
            x=self.r.get()
            self.s.put(x)
            i+=1
        x=self.r.get()
        self.count-=1
        self.s,self.r=self.r,self.s
        return x

    def top(self):
        if self.r.empty():
            return -1
        while not self.r.empty():
            x=self.r.get()
            self.s.put(x)
        self.s,self.r=self.r,self.s
        return x

#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1