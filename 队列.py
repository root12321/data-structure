class Queue(object):
    def __init__(self,tail=5,head=5):
        self.tail=tail
        self.S=[]
        self.head=head
def Enqueue(x):
    T.S.append(x)
    if T.tail>=5:
        T.tail=0
    else:
        T.tail=T.tail+1
    if len(T.S)>6:
        return 'upflow'
    if len(T.S)<0:
        return 'underflow'
    return T.S
def Dequeue(T):
    x=T.S.pop(0)
    if T.head==6:
        T.head=1
    else:
        T.head=T.head+1
    return x
T=Queue()
a=[1,2,3,4,7,6]
for i in a:
    print(Enqueue(i))
print(Dequeue(T))
print(Dequeue(T))
print(Dequeue(T))
print(Dequeue(T))
print(Dequeue(T))
print(Dequeue(T))
