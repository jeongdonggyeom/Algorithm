class queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.li = []
    
    def isEmpty(self):
        if self.rear == 0:
            return True
        else:
            return False
    
    def EnQueue(self, data):
        self.li.append(data)
        self.rear += 1
    
    def DeQueue(self):
        self.li.pop(self.front)
        self.rear -= 1
        
    def peek(self):
        return self.li[self.front]
    
test_q = queue()

print(test_q.isEmpty())

test_q.EnQueue(1)
test_q.EnQueue(2)
test_q.EnQueue(3)
test_q.EnQueue(4)
test_q.EnQueue(5)

print(test_q.isEmpty())
print(test_q.peek())
 
test_q.DeQueue()

print(test_q.peek())

test_q.DeQueue()
test_q.DeQueue()
test_q.DeQueue()
test_q.DeQueue()

print(test_q.isEmpty())