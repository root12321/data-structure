#定义红黑树
class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil
class RBTreeNode(object):
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size=None
#左旋转
def LeftRotate( T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    y.size=x.size
    x.size=x.left.size+x.right.size+1
#右旋转
def RightRotate( T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
    x.size=y.size
    y.size=y.left.size+y.right.size+1
#红黑树的插入
def RBInsert( T, z):
    z.left = T.nil
    z.right = T.nil
    z.parent = T.nil
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'red'
    z.size = 1#插入成功后 给Z付一个初始值1
    while z.parent!=T.nil:#每次插入一个值后，都要重新给插入的值更新一个size
        z.parent.size+=1
        z=z.parent
    RBInsertFixup(T,z)
#红黑树的上色
def RBInsertFixup( T, z):
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    LeftRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                RightRotate(T,z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    RightRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                LeftRotate(T, z.parent.parent)
    T.root.color = 'black'
#中序遍历
def Midsort(x):
    if x!= None:
        Midsort(x.left)
        if x.key!=0:
            print('key:', x.key,'x.parent',x.parent.key,'color:',x.color)
        Midsort(x.right)
#找到相应排名的元素
def OS_Select(x,i):
    r=x.left.size+1
    if i==r:
        return x
    elif i<r:
        return OS_Select(x.left,i)
    else:
        return OS_Select(x.right,i-r)
#找到相应元素的排名
def OS_Rank(x):
    r=x.left.size+1
    y=x
    while y!=T.root:
        if y==y.parent.right:
            r=r+y.parent.left.size+1
        y=y.parent
    return r
def Search(x,k):
    if x==T.nil or x.key==k:
        return x
    if k>x.key:
        return Search(x.right,k)
    else:
        return Search(x.left,k)
nodes = [11,2,14,1,7,15,5,8,4]
T = RBTree()
for node in nodes:
    RBInsert(T,RBTreeNode(node))
Midsort(T.root)
print(OS_Select(T.root,5).key)
print(OS_Rank(Search(T.root,7)))
