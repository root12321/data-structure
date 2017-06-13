#构造二叉树结构，及属性
class Tree(object):
    def __init__(self):
        self.root=None
class Node(object):
    def __init__(self,x):
        self.key=x
        self.left=None
        self.right=None
        self.parent=None
#插入二叉树数据
def TreeInsert( T, z):

    y =None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
#删除节点
def Transplant(T,u,v):
    if u.parent==None:
        T.root=v
    elif u==u.parent.left:
        u.parent.left=v
    else:
        u.parent.right=v
    if v!=None:
        v.parent=u.parent
def TreeMin(x):
    while x.left !=None:
        x=x.left
    return x
def TreeDelete(T,z):
    if z.left==None:
        Transplant(T,z,z.right)
    elif z.right==None:
        Transplant(T,z,z.left)
    else:
        y=TreeMin(z.right)
        if y.parent!=z:
            Transplant(T,y,y.right)
            y.right=z.right
            y.right.parent=y
        Transplant(T,z,y)
        y.left=z.left
        y.left.parent=y
#中序遍历
def Midsort(root):
    if root!= None:
        Midsort(root.left)
        if root.key!=0:
            print(root.key)
        Midsort(root.right)
#先序遍历
def Behsort(root):
    if root!= None:
        Behsort(root.left)
        Behsort(root.right)
        if root.key != 0:
            print(root.key)
#后序遍历
def Presort(root):
    if root!= None:
        if root.key != 0:
            print(root.key)
        Presort(root.left)
        Presort(root.right)
#构造二叉树实例对象
node=[5,9,6,8,7,2,1,10]
T=Tree()
#插入二叉树数据
for nodes in node:
    TreeInsert(T,Node(nodes))
#删去一个节点
TreeDelete(T,T.root)
#中序遍历
Midsort(T.root)
#后序遍历
Behsort(T.root)
#先序遍历
Presort(T.root)

