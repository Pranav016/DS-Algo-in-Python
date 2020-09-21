class Stack:

    def __init__(self):
        self.__data=[] # private empty list

    def push(self,item):
        self.__data.append(item)

    def pop(self):
        if self.__data is not self.empty():
            return self.__data.pop()
        else:
            print("Stack is empty")
            return

    def top(self):
        if self.__data is not self.empty():
            return self.__data[len(self.__data)-1]
        else:
            print("Stack is empty")
            return
    
    def empty(self):
        return len(self.__data)==0


# main
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
while not s.empty():
    print(s.pop())