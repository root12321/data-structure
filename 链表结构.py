class Lb(object):
    def __init__(self,key=None):
        self.key=key
        self.head=None
        self.prev=None
        self.next=None
def Search(k):
    x=L.head
    while x!=None and x.key!=k:
        x=x.next
    return x
def Insert(L,x):
    x.next=L.head
    if L.head!=None:
        L.head.prev=x
    L.head=x
    x.prev=None
    return x
def Delete(L,x):
    if x.prev!=None:
        x.prev.next=x.next
    else:
        L.head=x.next
    if x.next!=None:
        x.next.prev=x.prev
    return x
L=Lb()
a=[1,5,6,4,8,9,7]
for i in a:
    print(Insert(L,Lb(i)))
print(Delete(L,Search(1)))