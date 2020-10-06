class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map:
    def __init__(self):
        self.bucketSize=10
        self.bucket=[None for i in range(self.bucketSize)]
        self.count=0

    def size(self):
        return self.count
    
    def getIndex(self,hc):
        return (abs(hc)%(self.bucketSize))

    def insert(self,key,value):
        hc=hash(key)
        index=self.getIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        
        newNode=MapNode(key,value)
        newNode.next=head
        self.bucket[index]=newNode
        self.count+=1

    def getValue(self,key):
        hc=hash(key)
        index=self.getIndex(hc)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None

    def remove(self,key):
        hc=hash(key)
        index=self.getIndex(hc)
        head=self.bucket[index]
        prev=None
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.bucket[index]=head.next
                    val=head.value
                    del head
                    return val
                else:
                    prev.next=head.next
                    val=head.value
                    del head
                    return val
                prev.next=head
                head=head.next

# main
m=Map()
m.insert("Pranav1",10)
m.insert("Pranav2",20)
print("Size- ",m.size())
m.insert("Pranav3",30)
m.insert("Pranav2",40)
print("Size- ",m.size())
print("Search Value for 'Pranav2'- ",m.getValue("Pranav2"))
print("Search Value for 'Pranav3'- ",m.getValue("Pranav3"))
print("Remove 'Pranav3'- ",m.remove("Pranav3"))
print(m.getValue("Pranav3"))