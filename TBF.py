

# 初始化点
metrixs = {}

# 树类
def HST(r):
    """
    param r: 新的节点\n
    return: 以r为根结点的树\n
    """
    return [r]

def insertnode(r, newnode):
    """
    param r: 待插入节点的父亲结点\n
    param newnode: 新的孩子结点\n
    """
    # 直接在r列表的最后插入新的元素就行了，然后继续construct
    newHST = HST(newnode)
    r.append(newHST)



# 算法1
 


# 算法2

# 算法3

# 算法4