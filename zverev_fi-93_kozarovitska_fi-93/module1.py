class newNode:   
    def __init__(self, data,number):
        self.key = data
        self.count = []
        self.count.append(number)
        self.left = None
        self.right = None
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.key, root.count,
                                 end = " ")
        inorder(root.right)
def find_ns(root, lkpval, res):
      if lkpval < root.key:
         if self.left is None:
             a=1
            #return str(lkpval)+" Not Found"
         find_ns(root.left,lkpval,res)
      elif lkpval > root.key:
            if root.right is None:
                a=1
               #return str(lkpval)+" Not Found"
            find_ns(root.right, lkpval,res)
      else:
            res.append(root.count)
            if root.left is None:
                a=1
            elif root.left.key== lkpval:
                res.append(root.left.count)
                find_ns(root.left,lkpval,res)
            elif root.left is not None:
               find_ns( root.left, lkpval,res)
            if root.right is None:
                a=1
            elif root.right.key== lkpval:
                res.append(root.right.count)
                find_ns(root.right, lkpval,res)
            elif root.right is not None:
                find_ns(root.right,lkpval,res)
            return root.count
def insert(node, key, number):
    if node == None:
        k = newNode(key, number)
        return k
    if key == node.key:
        node.count.append(number)
        return node
    if key < node.key:
        node.left = insert(node.left, key, number)
    else:
        node.right = insert(node.right, key, number)
    return node
 
def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def deleteNode(root, key):
    if root == None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        root.count=[]
        if root.left == None:
            temp = root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.count = temp.count
        root.right = deleteNode(root.right, temp.key)
    return root
def deleteAll(root):
    root1=None
    
    return root1
def find(root, lkpval, res):
      if lkpval < root.key:
         if root.left is None:
            return str(lkpval)+" Not Found"
         find(root.left, lkpval, res)
      elif lkpval > root.key:
            if root.right is None:
               return str(lkpval)+" Not Found"
            find(root.right,lkpval,res)
      else:
          root.count.sort()
          for i in root.count:
              res.append(i)
          
          return root.count
def find_g(root,lkpval, res, res_key):
    if root != None:
        if root.key> lkpval:
            for i in root.count:
                res.append(i)
            res_key.append(root.key)
            find_g(root.left,lkpval, res, res_key)
        find_g(root.right,lkpval, res, res_key)
    res_key.sort()
    res.sort()
def find_l(root,lkpval, res, res_key):
    if root != None:
        if root.key< lkpval:
            for i in root.count:
                res.append(i)
            res_key.append(root.key)
            find_l(root.right,lkpval, res, res_key)
        find_l(root.left,lkpval, res, res_key)
    res_key.sort()
    res.sort()
def find_g_eq(root,lkpval, res, res_key):
    if root != None:
        if root.key>= lkpval:
            for i in root.count:
                res.append(i)
            res_key.append(root.key)
            find_g_eq(root.left,lkpval, res, res_key)
        find_g_eq(root.right,lkpval, res, res_key)
    res_key.sort()
    res.sort()
def find_l_eq(root,lkpval, res, res_key):
    if root != None:
        if root.key<= lkpval:
            for i in root.count:
                res.append(i)
            res_key.append(root.key)
            find_l_eq(root.right,lkpval, res, res_key)
        find_l_eq(root.left,lkpval, res, res_key)
    res_key.sort()
    res.sort()

