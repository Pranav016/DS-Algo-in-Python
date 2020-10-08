class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class PriorityQueue:
    def __init__(self):
        self.pq=[]

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize()==0
    
    def getMin(self):
        return self.pq[0].value

    def percolateUp(self):
        childIndex=self.getSize()-1
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if self.pq[childIndex].priority<self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
                childIndex=parentIndex
            else:
                break

    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.percolateUp()
        
    def percolateDown(self):
        parentIndex=0
        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*parentIndex+2

        while leftChildIndex < self.getSize():
            minIndex=parentIndex
            if self.pq[minIndex].priority>self.pq[leftChildIndex].priority:
                minIndex=leftChildIndex
            if rightChildIndex<self.getSize() and self.pq[minIndex].priority>self.pq[rightChildIndex].priority:
                minIndex=rightChildIndex
            if minIndex==parentIndex:
                break
            self.pq[minIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[minIndex]
            parentIndex=minIndex
            leftChildIndex=2*parentIndex+1
            rightChildIndex=2*parentIndex+2
    
    def removeMin(self):
        if self.isEmpty():
            return 
        ele=self.pq[0].value
        self.pq[self.getSize()-1],self.pq[0]=self.pq[0],self.pq[self.getSize()-1]
        self.pq.pop()
        self.percolateDown()
        return ele

        
# main
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1