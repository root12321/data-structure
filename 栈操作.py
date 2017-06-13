class Stack(object):
    def __init__(self,S=[],top=-1):
        self.S=S
        self.top=top
def Push(x):
    T.top=T.top+1
    T.S.append(x)
    return T.S
def Stack_Empty(T):
    if T.top==-1:
        return True
    else:
        return False
def Pop(T):
    if Stack_Empty(T):
        return 'error\'underflow\''
    else:
        T.top = T.top - 1
        return T.S.pop()

T=Stack()
a=[1,2,4,5,8,6]
for n in a:
    print(Push(n))
print(Pop(T))
print(Pop(T))
print(Pop(T))
print(Pop(T))
print(Pop(T))
print(Pop(T))
print(Pop(T))
