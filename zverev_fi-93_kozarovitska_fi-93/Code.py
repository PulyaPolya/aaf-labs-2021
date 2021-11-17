import re
def beatiful_print( column_names, columns, indexes_of_right_col, right_rows):
    if not right_rows:
        print("selection is empty")
    else:
        size = len(column_names)
        size_col=len(columns[0])
        max=[]
        for i in range(size):
                max.append(len(column_names[i]))
        
        print('\n')
        for j in right_rows:
                for i in indexes_of_right_col:
                    if len(columns[i][j])>max[i]:
                        max[i]=len(columns[i][j])
        #print(max)
        
        for i in indexes_of_right_col:
                t= max[i]-len(column_names[i])
                if (t%2==0):
                    print ("|", end='')
                    k=0
                    while k < t/2:
                        print (" ", end='')
                        k=k+1
                    print(column_names[i], end='')
                    k=0
                    while k < t/2:
                        print (" ", end='')
                        k=k+1
                 
                else:
                    print ("|", end='')
                    k=0
                    while k < t/2-1:
                        print (" ", end='')
                        k=k+1
                    print(column_names[i], end='')
                    k=0
                    while k < t/2:
                        print (" ", end='')
                        k=k+1
        print ("|", end='') 
        print('\n')
        print ("+", end='')
        for i in indexes_of_right_col:
            k=0
            while k<max[i]:
                print ("-",end='')
                k=k+1
            print ("+", end='')
        print('\n')
        for j in right_rows:
                for i in indexes_of_right_col:
                    t= max[i]-len(columns[i][j])
                    if (t%2==0):
                        print ("|", end='')
                        k=0
                        while k < t/2:
                            print (" ", end='')
                            k=k+1
                        print (columns[i][j], end='')
                        k=0
                        while k < t/2:
                            print (" ", end='')
                            k=k+1
                     
                    else:
                        print ("|", end='')
                        k=0
                        while k < t/2-1:
                            print (" ", end='')
                            k=k+1
                        print (columns[i][j], end='')
                        k=0
                        while k < t/2:
                            print (" ", end='')
                            k=k+1
                print ("|", end='') 
                print('\n')
        print ("+", end='')
        for i in indexes_of_right_col:
            k=0
            while k<max[i]:
                print ("-",end='')
                k=k+1
            print ("+", end='')
        print('\n')
def delete( column_names, columns, right_rows):
    size = len(column_names)
    size_col=len(columns[0])
    indexes_of_right_col=[]
    for i in range (len(column_names)):
             indexes_of_right_col.append(i)
    for j in reversed(right_rows):
            for i in reversed(indexes_of_right_col):
                    #columns[i][j]="*"
                    if columns[i]:
                        columns[i].pop(j)
                       
    #for i in indexes_of_right_col:
        #for element in columns[i]:
            #if element=="*":
               # columns[i].remove(element)
    
def delete_dupes(arr):
    size = len(arr)
    for i in range  (1,size):
        if i>= size:
            break
        if arr[i]==arr[i-1]:
            arr.pop(i)
            size= len(arr)
    size= len(arr)
    if size>2:
        if(arr[size-1]==arr[size-2]):
            arr.pop(size-1)
def delete_dupes_rand_order(arr):
    arr1=[]
    for i in reversed(arr):
        if i not in arr1:
                arr1.append(i)
    arr1.sort()
    arr=[]
    for elem in arr1:
        arr.append(elem)
    return arr
def edit_arr(arr):
    delete_dupes(arr)
    arr.sort()
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
            return str(lkpval)+" Not Found"
         return find_ns(root.left,lkpval,res)
      elif lkpval > root.key:
            if root.right is None:
               return str(lkpval)+" Not Found"
            return find_ns(root.right, lkpval,res)
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
     
    # If the tree is empty, return a new node
    if node == None:
        k = newNode(key, number)
        return k
 
    # If key already exists in BST, increment
    # count and return
    if key == node.key:
        node.count.append(number)
        return node
 
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key, number)
    else:
        node.right = insert(node.right, key, number)
 
    # return the (unchanged) node pointer
    return node
 
def minValueNode(node):
    current = node
 
    
    while current.left != None:
        current = current.left
 
    return current
 

def deleteNode(root, key):
     
    # base case
    if root == None:
        return root
 
    # If the key to be deleted is smaller than the
    # root's key, then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the key to be deleted is greater than
    # the root's key, then it lies in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)
 
    # if key is same as root's key
    else:
         
        # If key is present more than once,
        # simply decrement count and return
        
        root.count=[]
       # return root
         
        # ElSE, delete the node node with
        # only one child or no child
        if root.left == None:
            temp = root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp
 
        # node with two children: Get the inorder
        # successor (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's content
        # to this node
        root.key = temp.key
        root.count = temp.count
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
    return root
def find(root, lkpval, res):
      if lkpval < root.key:
         if root.left is None:
            return str(lkpval)+" Not Found"
         return find(root.left, lkpval, res)
      elif lkpval > root.key:
            if root.right is None:
               return str(lkpval)+" Not Found"
            return find(root.right,lkpval,res)
      else:
          edit_arr(root.count)
          for i in root.count:
              res.append(i)
          
          return root.count
            #print(str(self.data) + ' is found')
def find_g(root,lkpval, res, res_key):
    if root != None:
        find_g(root.left,lkpval, res, res_key)
       # print(root.key, root.count, end = " ")
        if root.key> lkpval:
            for i in root.count:
                res.append(i)
            res_key.append(root.key)
            #res.extend(root.count)
        find_g(root.right,lkpval, res, res_key)
    edit_arr(res_key)
    #print(res)
def find_g_eq(root,lkpval, res, res_key):
    find_g(root,lkpval, res, res_key)
    eq_res=[]
    find(root, lkpval,eq_res)
    for i in eq_res:
        res.append(i)
    res_key.append(lkpval)
    edit_arr(res)# this goes in order of appearing rows
    edit_arr(res_key)
def all_numbers(root, res, res_key):
    if root != None:
        all_numbers(root.left, res, res_key)
        #print(root.key, root.count,end = " ")
        for i in root.count:
            res.append(i)
        res_key.append(root.key)
        all_numbers(root.right, res, res_key)
def find_l(root,lkpval, res, res_key):
    all_arr=[]
    res_key_all=[]
    all_numbers(root,all_arr, res_key_all)
    geq_arr=[]
    res_key_geq=[]
    find_g_eq(root,lkpval, geq_arr, res_key_geq)
    for i in geq_arr:
        all_arr.remove(i)
    for i in res_key_geq:
        if i in res_key_all:
            res_key_all.remove(i)
    for t in all_arr:
        res.append(t)
    for t in  res_key_all:
        res_key.append(t)
    edit_arr(res_key)
def find_l_eq(root,lkpval, res, res_key):
    find_l(root,lkpval, res, res_key)
    eq_res=[]
    find(root, lkpval,eq_res)
    for i in eq_res:
        res.append(i)
    res_key.append(lkpval)
    edit_arr(res)
    edit_arr(res_key)
def deleteAll(root):
    root1=None
    return root1
class Table:
    size_table=0
    size_indexed=0
    def __init__(self, name, result, indexed, number_of_index):
        self.name= name
        self.numb_of_rows=1
        self.number=[]
        self.column_names=[]
        self.columns=[]
        self.indexed=[]
        self.number_of_index=[]
        self.size_indexed= len(indexed)
        for k in range (self.size_indexed):
            self.indexed.append(indexed[k])
            self.number_of_index.append(number_of_index[k])
        size = len(result)
        self.size_table=len(result)
        for i in range (size):
            self.columns.append(result[i])
            self.column_names.append(result[i])
            self.columns[i]=[]
    def add_row(self,number,result):
        if (len(self.number)==0):
            n=1
        else:
            n= max(self.number)+1
        self.number.append(n)
        #print(f"this is self.number {self.number}")
        size = len(self.column_names)
        size_col=len(self.columns[0])
        for i in range (size):
            self.columns[i].append(result[i])
        if number==1:
            for k in range (self.size_indexed):
                temp1=number_of_index[k]
                #print(result[temp1])
                self.indexed[k]=newNode(result[temp1],0)
        elif number !=1:
             for k in range (self.size_indexed):
                temp1=number_of_index[k]
                #print(result[temp1])
                self.indexed[k]=insert(self.indexed[k],result[temp1],n-1)
        self.numb_of_rows= self.numb_of_rows+1
       # self.column3.append(Row(value3))
    def get_name(self):
       return self.name
    def get_numb_of_rows(self):
        return self.numb_of_rows
    def get_col_name(self, arr):
        for i in range (self.size_table):
            arr.append(self.column_names[i])
    def get_size(self):
       return self.size_table
    def show1(self):
        size = len(self.column_names)
        size_col=len(self.columns[0])
        max=[]
        for i in range (size):
             max.append(len(self.column_names[i]))
        
        print('\n')
        for j in range (size_col):
             for i in range (size):
                 if len(self.columns[i][j])>max[i]:
                     max[i]=len(self.columns[i][j])
        print(max)
        
        for i in range (size):
             t= max[i]-len(self.column_names[i])
             if (t%2==0):
                 print ("|", end='')
                 k=0
                 while k < t/2:
                    print (" ", end='')
                    k=k+1
                 print(self.column_names[i], end='')
                 k=0
                 while k < t/2:
                    print (" ", end='')
                    k=k+1
                 
             else:
                 print ("|", end='')
                 k=0
                 while k < t/2-1:
                    print (" ", end='')
                    k=k+1
                 print(self.column_names[i], end='')
                 k=0
                 while k < t/2:
                    print (" ", end='')
                    k=k+1
        print ("|", end='') 
        print('\n')
        print ("+", end='')
        for i in max:
            k=0
            while k<i:
                print ("-",end='')
                k=k+1
            print ("+", end='')
        print('\n')
        for j in range (size_col):
             for i in range (size):
                 t= max[i]-len(self.columns[i][j])
                 if (t%2==0):
                     print ("|", end='')
                     k=0
                     while k < t/2:
                         print (" ", end='')
                         k=k+1
                     print (self.columns[i][j], end='')
                     k=0
                     while k < t/2:
                         print (" ", end='')
                         k=k+1
                     
                 else:
                     print ("|", end='')
                     k=0
                     while k < t/2-1:
                         print (" ", end='')
                         k=k+1
                     print (self.columns[i][j], end='')
                     k=0
                     while k < t/2:
                         print (" ", end='')
                         k=k+1
             print ("|", end='') 
             print('\n')
        print ("+", end='')
        for i in max:
            k=0
            while k<i:
                print ("-",end='')
                k=k+1
            print ("+", end='')
        print('\n')
    def show(self):
         indexes_of_right_col=[]
         right_rows=[]
         size_col=len(self.columns[0])
         for t in range (size_col):
             right_rows.append(t)
         for i in range (len(self.column_names)):
             indexes_of_right_col.append(i)
         edit_arr(indexes_of_right_col)
         edit_arr(right_rows)
         beatiful_print(self.column_names, self.columns,indexes_of_right_col,right_rows)#!!!!
    def delete_all(self):
         indexes_of_right_col=[]
         self.number=[]
         self.number_of_index=[]
         right_rows=[]
         for t in range (len(self.indexed)):
             self.indexed[t]=deleteAll(self.indexed[t])
         size_col=len(self.columns[0])
         for t in range (size_col):
             right_rows.append(t)
         for i in range (len(self.column_names)):
             indexes_of_right_col.append(i)
         edit_arr(indexes_of_right_col)
         edit_arr(right_rows)
         delete(self.column_names, self.columns, right_rows)
    def show_col(self, indexes_of_right_col):
        right_rows=[]
        size_col=len(self.columns[0])
        for t in range (size_col):
             right_rows.append(t)
        beatiful_print(self.column_names, self.columns, indexes_of_right_col,right_rows)
    def show_col1(self, indexes_of_right_col):
        size = len(self.column_names)
        size_col=len(self.columns[0])
        for i in indexes_of_right_col:
            print(self.column_names[i], end=' ')
        print('\n')
        for j in range (size_col):
             for i in  indexes_of_right_col:
                 print (self.columns[i][j], end=' ')
             print('\n')
    def show_col_where(self, col_mumbers, number, symbol, value):
           size = len(self.column_names)
           size_col=len(self.columns[0])
           numb_of_rows=[]
           numb =-1 # number column, which is indexed and in which we need to find value
           for t in range (len(self.number_of_index)):
               if number==self.number_of_index[t]:
                   numb=t
                   break
           if numb>=0:                  # that means that we found smth indexed
               right_rows=[] #array for number of indexed columns, which we need to print
               #self.indexed[t].PrintTree()
               right_arr_rows=[]
               res_temp=[]
               if (symbol=="="):
                   find(self.indexed[t], value, right_rows)
                   edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   beatiful_print(self.column_names,self.columns,col_mumbers, right_arr_rows)
               elif (symbol=="<"):
                   find_l(self.indexed[t],value, right_rows,res_temp)
                   edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   beatiful_print(self.column_names,self.columns,col_mumbers, right_arr_rows)
               elif (symbol=="<="):
                   find_l_eq( self.indexed[t],value, right_rows,res_temp)
                   edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   beatiful_print(self.column_names,self.columns,col_mumbers, right_arr_rows)
               elif (symbol==">"):
                   find_g(self.indexed[t],value, right_rows,res_temp)
                   edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   beatiful_print(self.column_names,self.columns,col_mumbers, right_arr_rows)
               elif (symbol==">="):
                   find_g_eq(self.indexed[t],value, right_rows,res_temp)
                   edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   beatiful_print(self.column_names,self.columns,col_mumbers, right_arr_rows)
           else:
               res_temp=[]
               right_rows=[]
               if (symbol=="="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]==value:
                            right_rows.append(k)
               elif (symbol=="<"):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]<value:
                            right_rows.append(k)
               elif (symbol=="<="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]<=value:
                            right_rows.append(k)
               elif (symbol==">"):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]>value:
                            right_rows.append(k)
               elif (symbol==">="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]>=value:
                            right_rows.append(k)
               beatiful_print(self.column_names,self.columns,col_mumbers, right_rows)
    def show_col_where_two_col(self,col_mumbers, number1,number2, symbol):
        right_rows=[]
        if (symbol=="="):
            for k in range (len(self.columns[0])):
                if self.columns[number1][k]==self.columns[number2][k]:
                    right_rows.append(k)
        elif (symbol=="<"):
                   for k in range (len(self.columns[number])):
                       if self.columns[number1][k]<self.columns[number2][k]:
                            right_rows.append(k)
        elif (symbol=="<="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number1][k]<=self.columns[number2][k]:
                            right_rows.append(k)
        elif (symbol==">"):
                   for k in range (len(self.columns[number])):
                       if self.columns[number1][k]>self.columns[number2][k]:
                            right_rows.append(k)
        elif (symbol==">="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number1][k]>=self.columns[number2][k]:
                            right_rows.append(k)
        beatiful_print(self.column_names,self.columns,col_mumbers, right_rows)
    def  delete_col_where(self, number, symbol, value):
           size = len(self.column_names)
           size_col=len(self.columns[0])
           numb_of_rows=[]
           numb =-1 # number column, which is indexed and in which we need to find value
           for t in range (len(self.number_of_index)):
               if number==self.number_of_index[t]:
                   numb=t
                   break
           if numb>=0:                  # that means that we found smth indexed
               right_rows=[] #array for number of indexed columns, which we need to print
               #self.indexed[t].PrintTree()
               key_values=[]
               right_arr_rows=[]
               if (symbol=="="):
                   find(self.indexed[t], value, right_rows) # finds numbers of value in tree
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   deleteNode(self.indexed[t], value)
                   #inorder(self.indexed[t])
                   edit_arr(right_rows)
                   print(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_arr_rows)
               elif (symbol=="<"):
                   find_l(self.indexed[t],value, right_rows, key_values)
                   for k in right_rows:
                    edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   for a in key_values:
                       deleteNode(self.indexed[t], a)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_arr_rows)
                   print(self.number)
               elif (symbol=="<="):
                   find_l_eq(self.indexed[t],value, right_rows, key_values)
                   for k in right_rows:
                    edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   for a in key_values:
                       deleteNode(self.indexed[t], a)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_arr_rows)
               elif (symbol==">"):
                   find_g(self.indexed[t],value, right_rows, key_values)
                   for k in right_rows:
                    edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   for a in key_values:
                       deleteNode(self.indexed[t], a)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_arr_rows)
               elif (symbol==">="):
                   find_g_eq(self.indexed[t],value, right_rows, key_values)
                   for k in right_rows:
                    edit_arr(right_rows)
                   for j in right_rows:  
                       for k in range (len(self.number)):
                           if j+1==self.number[k]:
                               right_arr_rows.append(k)
                   for a in key_values:
                       deleteNode(self.indexed[t], a)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_arr_rows)
               print(f"this is self.number {self.number}")
          # for i in right_rows:
             #  self.number.remove(i+1)
           else:
               right_rows=[]
               if (symbol=="="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]==value:
                            right_rows.append(k)
               elif (symbol=="<"):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]<value:
                            right_rows.append(k)
               elif (symbol=="<="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]<=value:
                            right_rows.append(k)
               elif (symbol==">"):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]>value:
                            right_rows.append(k)
               elif (symbol==">="):
                   for k in range (len(self.columns[number])):
                       if self.columns[number][k]>=value:
                            right_rows.append(k)
               delete(self.column_names,self.columns, right_rows)
    def delete_col_where_two_col(self, number1,number2, symbol):
               key_values=[]
               right_rows=[]
               if (symbol=="="):
                   #find(self.indexed[t], value, right_rows) # finds numbers of value in tree
                   for k in range (len(self.columns[0])):
                        if self.columns[number1][k]==self.columns[number2][k]:
                             right_rows.append(k)
                             value=self.columns[number1][k]
                   for t in range (len(self.number_of_index)):
                       if number1==self.number_of_index[t]:
                           deleteNode(self.indexed[t], value)
                   for t in range (len(self.number_of_index)):
                       if number2==self.number_of_index[t]:
                           deleteNode(self.indexed[t], value)
                   #inorder(self.indexed[t])
                   edit_arr(right_rows)
                   print(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_rows)
               elif (symbol=="<"):
                   values1=[]
                   values2=[]
                   for k in range (len(self.columns[0])):
                        if self.columns[number1][k]<self.columns[number2][k]:
                             right_rows.append(k)
                             values1.append(self.columns[number1][k])
                             values2.append(self.columns[number2][k])
                   for t in range (len(self.number_of_index)):
                       if number1==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   for t in range (len(self.number_of_index)):
                       if number2==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   #inorder(self.indexed[t])
                   edit_arr(right_rows)
                  # print(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_rows)
               elif (symbol=="<="):
                   values1=[]
                   values2=[]
                   for k in range (len(self.columns[0])):
                        if self.columns[number1][k]<=self.columns[number2][k]:
                             right_rows.append(k)
                             values1.append(self.columns[number1][k])
                             values2.append(self.columns[number2][k])
                   for t in range (len(self.number_of_index)):
                       if number1==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   for t in range (len(self.number_of_index)):
                       if number2==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_rows)
               elif (symbol==">"):
                   values1=[]
                   values2=[]
                   for k in range (len(self.columns[0])):
                        if self.columns[number1][k]>self.columns[number2][k]:
                             right_rows.append(k)
                             values1.append(self.columns[number1][k])
                             values2.append(self.columns[number2][k])
                   for t in range (len(self.number_of_index)):
                       if number1==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   for t in range (len(self.number_of_index)):
                       if number2==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_rows)
               elif (symbol==">="):
                   values1=[]
                   values2=[]
                   for k in range (len(self.columns[0])):
                        if self.columns[number1][k]>=self.columns[number2][k]:
                             right_rows.append(k)
                             values1.append(self.columns[number1][k])
                             values2.append(self.columns[number2][k])
                   for t in range (len(self.number_of_index)):
                       if number1==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   for t in range (len(self.number_of_index)):
                       if number2==self.number_of_index[t]:
                           for value in values1:
                            deleteNode(self.indexed[t], value)
                   edit_arr(right_rows)
                   for m in right_rows:
                       self.number.remove(m+1)
                   delete(self.column_names,self.columns, right_rows)
               print(f"this is self.number {self.number}")
    def show_col_where1(self, col_mumbers, number, value):
           size = len(self.column_names)
           size_col=len(self.columns[0])
           numb_of_rows=[]
           numb =-1 # number column, which is indexed and in which we need to find value
           for t in range (len(self.number_of_index)):
               if number==self.number_of_index[t]:
                   numb=t
                   break
           if numb>0:                  # that means that we found smth indexed
               right_rows=[] #array for number of indexed columns, which we need to print
              # self.indexed[t].PrintTree()
               self.indexed[t].findval(value, right_rows)
               delete_dupes(right_rows)
               print(right_rows)
               for i in col_mumbers:
                    print(self.column_names[i], end=' ')
               print('\n')
               for j in right_rows:
                    for i in  col_mumbers:
                        print (self.columns[i][j-1], end=' ')
                    print('\n')
           else:
               for k in range (len(self.columns[number])):
                   if self.columns[number][k]==value:
                       numb_of_rows.append(k)
               for i in col_mumbers:
                    print(self.column_names[i], end=' ')
               print('\n')
               for j in numb_of_rows:
                    for i in  col_mumbers:
                        print (self.columns[i][j], end=' ')
                    print('\n') 
    def delete_col_where1(self, col_mumbers, number, value):
           size = len(self.column_names)
           size_col=len(self.columns[0])
           numb_of_rows=[]
           numb =-1 # number column, which is indexed and in which we need to find value
           for t in range (len(self.number_of_index)):
               if number==self.number_of_index[t]:
                   numb=t
                   break
           if numb>0:                  # that means that we found smth indexed
               right_rows=[] #array for number of indexed columns, which we need to print
               self.indexed[t].PrintTree()
               self.indexed[t].findval(value, right_rows)
               delete_dupes(right_rows)
               print(right_rows)
               for i in col_mumbers:
                    print(self.column_names[i], end=' ')
               print('\n')
               for j in right_rows:
                    for i in  col_mumbers:
                        print (self.columns[i][j-1], end=' ')
                    print('\n')
           else:
               for k in range (len(self.columns[number])):
                   if self.columns[number][k]==value:
                       numb_of_rows.append(k)
               for i in col_mumbers:
                    print(self.column_names[i], end=' ')
               print('\n')
               for j in numb_of_rows:
                    for i in  col_mumbers:
                        print (self.columns[i][j], end=' ')
                    print('\n') 

table_names=[]
EmpInput = ""
table_name = ""
id = ""
tables =[]
print("Шаблон ввода данных : CREATE ИМЯ_ТАБЛИЦЫ (id(число))")
KeyWords = ['create','select','insert']
while ";" not in EmpInput:
    EmpInput += input()
    EmpInput+='  '
col_numb=0
EmpInput1=EmpInput
EmpInput1=EmpInput1.casefold()
while "exit" not in EmpInput1:
    EmpInput1=EmpInput
    EmpInput1=EmpInput1.casefold()
    if ("create" in EmpInput1):
        #result = re.match(r'\s*(C|c)(r|R)(e|E)(A|a)(t|T)(e|E)\s+[a-zA-Z][a-zA-Z0-9]*\s*\(\s*([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\)\s*', EmpInput)
        #result = re.match(r'create\s+[a-zA-Z0-9]+\s*\(\s*[a-zA-Z0-9]+\s*,\s*[a-zA-Z0-9]+\s*\)\s*', EmpInput)
        s1='\s*(C|c)(r|R)(e|E)(A|a)(t|T)(e|E)\s+[a-zA-Z][a-zA-Z0-9]*\s*\(\s*([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\)\s*'
        if re.match(s1, EmpInput) is not None:
            temp=re.sub(r'(C|c)(r|R)(e|E)(A|a)(t|T)(e|E)',' create ', EmpInput)
            temp=re.sub(r'(I|i)(N|n)(D|d)(E|e)(X|x)(e|E)(D|d)','indexed', temp)
            #temp = result.group(0)
            temp = temp.replace("create","",1) #\s+[a-z]{1,10}\s+\([a-z]{1,10},[a-z]{1,10}\)
            temp = temp.replace("("," ")
            temp = temp.replace(")"," ")
            temp = temp.replace(" ","",1)
            temp = temp.replace(","," ")
            temp = temp.replace(";"," ")
            result = str.split(temp) # название таблицы re.split(r" ", temp)
            table_names.append('@')
            try:
                for words in table_names:#!!!!!!!
                     if result[0]==words:
                        raise ValueError("this name is already taken")
                     else:
                        for elem in KeyWords:
                            try:
                             if result[0]==elem:
                                raise Exception("cant't use key words")
                            except Exception as error:
                                print('cant use key words')
                        name_table= result[0]
                        index=[]
                        number_of_index=[]
                        size = len(result)
                        i=0
                        while i<size:
                           if result[i]=="indexed":
                               index.append(result[i-1])
                               number_of_index.append(i-2)
                               result.pop(i)
                               size=len(result) 
                           i=i+1
                        size = len(result)
                        size = len(index)
                        result.pop(0)
                        table_names.append(name_table)
                        name_table1=name_table
                        name_table= Table(name_table, result, index,number_of_index)
                        print(f"Table {name_table1} has been created")
            
                        tables.append(name_table)
                        arr=[]
                        size= len(result)
                        name_table.get_col_name(arr)
                        break
            except ValueError:
                    print("this name is already taken")

        EmpInput=""
        while ";" not in EmpInput:
            EmpInput += input()
            EmpInput+='  '
        temp = ""
    elif ("insert" in EmpInput1):
        s1='\s*(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)\s+[a-zA-Z0-9]+\s*\(\s*("[^"]+"\s*,\s*)*("[^"]+"\s*)\)\s*'
        #result1 = re.match(r'\s*(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)\s+[a-zA-Z0-9]+\s*\(\s*("[^"]+"\s*,\s*)*("[^"]+"\s*)\)\s*', EmpInput)
        #temp = result1.group(0)
        if re.match(s1, EmpInput) is not None:
            temp1=re.findall(r'\"[^\"]+\"', EmpInput)
            column_values=[]
            temp=re.sub(r'(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)','  insert  ', EmpInput)
            #temp2=result2.group(0)
            for elem in temp1:
                    elem=elem.replace('"','')
                    column_values.append(elem)
            temp = temp.replace('"','')
            temp = temp.replace("insert","",1) # ''
            temp = temp.replace("("," ")
            temp = temp.replace(")","")
            temp = temp.replace(" ","",1)
            temp = temp.replace(","," ")
            result1 = str.split(temp) # название таблицы 
            for elem in KeyWords:
                if result1[0]==elem:
                    raise Exception("cant't use key words")
            check_if_name_is_right=-1
            for elem in tables:
              if elem.get_name()==result1[0]:
                    name_of_insert= elem.get_name()
                    check_if_name_is_right=1
                    break
            try:
                if check_if_name_is_right==-1:
                    raise Exception("wrong name")
                else:
            #for elem in tables:
               # if elem.get_name()==result1[0]:
                    #name_of_insert= elem.get_name()
                    #break
                    col_numb= elem.get_numb_of_rows()
                    result1.pop(0)
                    try:
                        if(elem.get_size()!=len(column_values)):
                            raise Exception("wrong size")
                        else:
                            r1= elem.add_row(col_numb, column_values)
                            print(f"Row has been added to table {name_of_insert}")
                    except Exception:
                            print("wrong size")
            except Exception:
                print("wrong name")
               # print(col_numb)
        EmpInput=""
        while ";" not in EmpInput:
            EmpInput += input()
            EmpInput+='  '
    
    elif ("select" in EmpInput1):
        if ("*" in EmpInput1):
            if ("where" in EmpInput1):
                s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*(w|W)(h|H)(e|E)(r|R)(e|E)\s+([a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*(\"[^\"]+\"\s*))'
                s2='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) \s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
                s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) \s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
                if re.match(s1, EmpInput) is not None:
                    temp=EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ', temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
                    temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ',  temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace(";","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    if ("<=" in EmpInput):
                         temp = temp.replace("<="," <= ")
                    elif (">=" in EmpInput):
                        temp = temp.replace(">="," >=  ")
                    elif (">" in EmpInput):
                        temp = temp.replace(">"," > ")
                    elif ("<" in EmpInput):
                        temp = temp.replace("<"," <  ")
                    elif ("=" in EmpInput):
                        temp = temp.replace("="," =  ")
                    result1 = str.split(temp) # название таблицы 
                    size = len(result1)
                    for i in range (len(result1)):
                        if result1[i]=="where":
                             name_of_insert=result1[i-1]
                             result1.pop(i-1)
                             #temp = temp.replace(name_of_insert," ")
                             break
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==name_of_insert:
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            
                            #print(name_of_insert)
                            temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            number=0
                            size_res=len(result1)
                            temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            result1.pop(len(result1)-4)
                            col_names=[]
                            indexes=[]
                            elem.get_col_name(col_names)
                            size_col_names= len(col_names)
                            size_res= len(result1)
                            number=0
                            size_res=len(result1)
                            for k in range (size_res-2):
                                for i in range (size_col_names):
                                    #if col_names[i]==result1[k]:
                                    indexes.append(i)
                                    if col_names[i]==result1[size_res-3]:
                                        number=i+1
                            result1.pop(size_res-3)
                            try:
                                if number ==0:
                                    raise Exception("wrong column")
                                else:
                                    delete_dupes(indexes)
                                    indexes=delete_dupes_rand_order(indexes)
                                    size_res=len(result1)
                                    try:
                                        print(f"this is {elem.get_name()} table")
                                        elem.show_col_where(indexes, number-1,result1[size_res-2], result1[size_res-1])
                                    except :
                                        print("something vemt wrong")
                            except Exception:
                                print("wrong column")
                    except Exception:
                        print("wrong name")
                    EmpInput=""
                    number=0
                    EmpInput=""
                elif re.match(s2, EmpInput) is not None:
                    temp=EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ',  temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
                    temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ',  temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace(";","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    if ("<=" in EmpInput):
                         temp = temp.replace("<="," >= ")
                    elif (">=" in EmpInput):
                        temp = temp.replace(">="," <=  ")
                    elif (">" in EmpInput):
                        temp = temp.replace(">"," < ")
                    elif ("<" in EmpInput):
                        temp = temp.replace("<"," >  ")
                    elif ("=" in EmpInput):
                        temp = temp.replace("="," =  ")
                    result1 = str.split(temp) # название таблицы 
                
                    size = len(result1)
                    for i in range (len(result1)):
                        if result1[i]=="where":
                             name_of_insert=result1[i-1]
                             result1.pop(i-1)
                             #temp = temp.replace(name_of_insert," ")
                             break
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==name_of_insert:
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            
                            #print(name_of_insert)
                            temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            number=0
                            size_res=len(result1)
                            temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            result1.pop(len(result1)-4)
                        #print(result1)
                            col_names=[]
                            indexes=[]
                            elem.get_col_name(col_names)
                            size_col_names= len(col_names)
                            size_res= len(result1)
                            number=0
                            size_res=len(result1)
                            for k in range (size_res):
                                for i in range (size_col_names):
                                   #if col_names[i]==result1[k]:
                                    indexes.append(i)
                                    if col_names[i]==result1[size_res-1]:
                                        number=i+1
                            result1.pop(size_res-1)
                            indexes.pop(len(indexes)-1)
                            try:
                                if number ==0:
                                    raise Exception("wrong column")
                                else:
                                    size_res=len(result1)
                                    indexes=delete_dupes_rand_order(indexes)
                                    try:
                                        print(f"this is {elem.get_name()} table")
                                        elem.show_col_where(indexes, number-1,result1[size_res-1], result1[size_res-2])
                                    except:
                                        print("smth went wrong")
                            except Exception:
                                print("wrong column")
                    except Exception:
                        print('wrong name')
                elif re.match(s3, EmpInput) is not None:
                    temp=EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ', temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
                    temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ',  temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace(";","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    if ("<=" in EmpInput):
                         temp = temp.replace("<="," <= ")
                    elif (">=" in EmpInput):
                        temp = temp.replace(">="," >=  ")
                    elif (">" in EmpInput):
                        temp = temp.replace(">"," > ")
                    elif ("<" in EmpInput):
                        temp = temp.replace("<"," <  ")
                    elif ("=" in EmpInput):
                        temp = temp.replace("="," =  ")
                    result1 = str.split(temp) # название таблицы 
                    size = len(result1)
                    for i in range (len(result1)):
                        if result1[i]=="where":
                             name_of_insert=result1[i-1]
                             result1.pop(i-1)
                             #temp = temp.replace(name_of_insert," ")
                             break
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==name_of_insert:
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            number=0
                            size_res=len(result1)
                            #temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            result1.pop(len(result1)-4)
                            col_names=[]
                            indexes=[]
                            elem.get_col_name(col_names)
                            size_col_names= len(col_names)
                            size_res= len(result1)
                            number1=0
                            number2=0
                            size_res=len(result1)
                            for k in range (size_res-2):
                                for i in range (size_col_names):
                                    #if col_names[i]==result1[k]:
                                    indexes.append(i)
                                    if col_names[i]==result1[size_res-3]:
                                        number1=i+1
                                    if col_names[i]==result1[size_res-1]:
                                        number2=i+1
                            result1.pop(size_res-3)
                            try:
                                if number1==0:
                                    raise Exception("wrong column")
                                if number2==0:
                                    raise Exception("wrong column")
                                else:
                                    delete_dupes(indexes)
                                    indexes=delete_dupes_rand_order(indexes)
                                    size_res=len(result1)
                                    try:
                                        print(f"this is {elem.get_name()} table")
                                        elem.show_col_where_two_col(indexes, number1-1, number2-1, result1[size_res-2])
                                    except :
                                        print("something vemt wrong")
                            except Exception:
                                print("wrong column")
                    except Exception:
                        print("wrong name")
                    EmpInput=""
                    number=0
                    EmpInput=""
                EmpInput=""
                
            else:
                s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*'
                #result1 = re.match(r'\s*select\s+\*\s+from\s+[a-zA-Z0-9]+\s*', EmpInput)
                if re.match(s1, EmpInput) is not None:
                    temp = EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ',  temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    temp = temp.replace(";"," ")
                    result1 = str.split(temp) # название таблицы 
                    for elem in KeyWords:
                        if result1[0]==elem:
                            raise Exception("cant't use key words")
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==result1[1]:
                            name_of_insert= elem.get_name()
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            print(f"this is {elem.get_name()} table")
                            try:
                                elem.show()
                            except:
                                print("smth went wrong")
                    except Exception: 
                        print('wrong name')
            EmpInput=""
            while ";" not in EmpInput:
                EmpInput += input()
                EmpInput+='  '
        elif ("where" in EmpInput1):
            #try:
                result1=[]
                s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*("[^"]+"\s*)'
               # s1='select\s+([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+from\s+[a-zA-Z0-9]+\s* where\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*("[^"]+"\s*)'
                s2='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) ([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+("[^"]+"\s*)((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
                s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) ([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
                if re.match(s1, EmpInput) is not None:
                    temp=EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ', temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
                    temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ', temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace(";","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    if ("<=" in EmpInput):
                         temp = temp.replace("<="," <= ")
                    elif (">=" in EmpInput):
                        temp = temp.replace(">="," >=  ")
                    elif (">" in EmpInput):
                        temp = temp.replace(">"," > ")
                    elif ("<" in EmpInput):
                        temp = temp.replace("<"," <  ")
                    elif ("=" in EmpInput):
                        temp = temp.replace("="," =  ")
                    result1 = str.split(temp) # название таблицы 
                
                    size = len(result1)
                    for i in range (len(result1)):
                        if result1[i]=="where":
                             name_of_insert=result1[i-1]
                             result1.pop(i-1)
                             #temp = temp.replace(name_of_insert," ")
                             break
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==name_of_insert:
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            print(f"this is {elem.get_name()} table")
                            #print(name_of_insert)
                            temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            number=0
                            size_res=len(result1)
                            temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            result1.pop(len(result1)-4)
                        #print(result1)
                            col_names=[]
                            indexes=[]
                            elem.get_col_name(col_names)
                            size_col_names= len(col_names)
                            size_res= len(result1)
                            number=0
                            size_res=len(result1)
                            for k in range (size_res-2):
                                for i in range (size_col_names):
                                    if col_names[i]==result1[k]:
                                        indexes.append(i)
                                    if col_names[i]==result1[size_res-3]:
                                        number=i+1
                            result1.pop(size_res-3)
                            indexes.pop(len(indexes)-1)
                            try:
                                for i in range (len(indexes)-1):
                                    if indexes[i+1]<indexes[i]:
                                         raise Exception("wrong order")
                                if len(indexes)<(len(result1)-3):
                                    raise Exception("wrong")
                                if number ==0:
                                    raise Exception("wrong column")
                                else:
                                    size_res=len(result1)
                                    try:
                                        elem.show_col_where(indexes, number-1,result1[size_res-2], result1[size_res-1])
                                    except:
                                        print("smth went wrong")
                            except Exception:
                                print("smth went wrong")
                    except Exception:
                        print("you have inserted the wrong name")
                    EmpInput=""
                    number=0
                elif re.match(s2, EmpInput) is not None:
                    temp=EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ',  temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
                    temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ',  temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace(";","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    if ("<=" in EmpInput):
                         temp = temp.replace("<="," >= ")
                    elif (">=" in EmpInput):
                        temp = temp.replace(">="," <=  ")
                    elif (">" in EmpInput):
                        temp = temp.replace(">"," < ")
                    elif ("<" in EmpInput):
                        temp = temp.replace("<"," >  ")
                    elif ("=" in EmpInput):
                        temp = temp.replace("="," =  ")
                    result1 = str.split(temp) # название таблицы 
                
                    size = len(result1)
                    for i in range (len(result1)):
                        if result1[i]=="where":
                             name_of_insert=result1[i-1]
                             result1.pop(i-1)
                             #temp = temp.replace(name_of_insert," ")
                             break
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==name_of_insert:
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            print(f"this is {elem.get_name()} table")
                            #print(name_of_insert)
                            temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            number=0
                            size_res=len(result1)
                            temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            result1.pop(len(result1)-4)
                        #print(result1)
                            col_names=[]
                            indexes=[]
                            elem.get_col_name(col_names)
                            size_col_names= len(col_names)
                            size_res= len(result1)
                            number=0
                            size_res=len(result1)
                            for k in range (size_res):
                                for i in range (size_col_names):
                                    if col_names[i]==result1[k]:
                                        indexes.append(i)
                                    if col_names[i]==result1[size_res-1]:
                                        number=i+1
                            result1.pop(size_res-1)
                            indexes.pop(len(indexes)-1)
                            try:
                                for i in range (len(indexes)-1):
                                    if indexes[i+1]<indexes[i]:
                                         raise Exception("wrong order")
                                if len(indexes)<(len(result1)-3):
                                    raise Exception("wrong")
                                if number ==0:
                                    raise Exception("wrong column")
                                else:
                            #delete_dupes(indexes)
                                    size_res=len(result1)
                                    try:
                                        elem.show_col_where(indexes, number-1,result1[size_res-1], result1[size_res-2])
                                    except:
                                        print("smth went wrong")
                            except Exception:
                                print("smth went wrong")
                    except Exception:
                        print("you have inserted the wrong name")
                elif re.match(s3, EmpInput) is not None:
                    temp=EmpInput
                    temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ',  temp)
                    temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
                    temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ',  temp)
                    temp = temp.replace("select","",1)
                    temp = temp.replace(";","",1)
                    temp = temp.replace("from","",1)
                    temp = temp.replace(" ","",1)
                    temp = temp.replace(","," ")
                    if ("<=" in EmpInput):
                         temp = temp.replace("<="," <= ")
                    elif (">=" in EmpInput):
                        temp = temp.replace(">="," >=  ")
                    elif (">" in EmpInput):
                        temp = temp.replace(">"," > ")
                    elif ("<" in EmpInput):
                        temp = temp.replace("<"," <  ")
                    elif ("=" in EmpInput):
                        temp = temp.replace("="," =  ")
                    result1 = str.split(temp) # название таблицы 
                
                    size = len(result1)
                    for i in range (len(result1)):
                        if result1[i]=="where":
                             name_of_insert=result1[i-1]
                             result1.pop(i-1)
                             #temp = temp.replace(name_of_insert," ")
                             break
                    check_if_name_is_right=-1
                    for elem in tables:
                        if elem.get_name()==name_of_insert:
                            check_if_name_is_right=1
                            break
                    try:
                        if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                        else:
                            
                            #print(name_of_insert)
                            temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            number=0
                            size_res=len(result1)
                            temp = temp.replace('"'," ")
                            result1 = str.split(temp)
                            result1.pop(len(result1)-4)
                        #print(result1)
                            col_names=[]
                            indexes=[]
                            elem.get_col_name(col_names)
                            size_col_names= len(col_names)
                            size_res= len(result1)
                            number1=0
                            number2=0
                            size_res=len(result1)
                            for k in range (size_res-2):
                                for i in range (size_col_names):
                                    if col_names[i]==result1[k]:
                                        indexes.append(i)
                                    if col_names[i]==result1[size_res-3]:
                                        number1=i+1
                                    if col_names[i]==result1[size_res-1]:
                                        number2=i+1
                            result1.pop(size_res-1)
                            indexes.pop(len(indexes)-1)
                            try:
                                for i in range (len(indexes)-1):
                                    if indexes[i+1]<indexes[i]:
                                         raise Exception("wrong order")
                                if len(indexes)<(len(result1)-3):
                                    raise Exception("wrong")
                                if number1 ==0:
                                    raise Exception("wrong column")
                                if number2 ==0:
                                    raise Exception("wrong column")
                                else:
                            #delete_dupes(indexes)
                                    size_res=len(result1)
                                    try:
                                        print(f"this is {elem.get_name()} table")
                                        elem.show_col_where_two_col(indexes, number1-1, number2-1, result1[size_res-1])
                                    except:
                                        print("smth went wrong")
                            except Exception:
                                print("smth went wrong")
                    except Exception:
                        print("you have inserted the wrong name")
                """
                temp=EmpInput
                temp = temp.replace("select","",1)
                temp = temp.replace(";","",1)
                temp = temp.replace("from","",1)
                temp = temp.replace(" ","",1)
                temp = temp.replace(","," ")
                
                #temp = temp.replace("="," = ",1)
                #temp = temp.replace("<"," < ",1)
                if ("<=" in EmpInput):
                     temp = temp.replace("<="," <= ")
                elif (">=" in EmpInput):
                    temp = temp.replace(">="," >=  ")
                elif (">" in EmpInput):
                    temp = temp.replace(">"," > ")
                elif ("<" in EmpInput):
                    temp = temp.replace("<"," <  ")
                elif ("=" in EmpInput):
                    temp = temp.replace("="," =  ")
                result1 = str.split(temp) # название таблицы 
                
                size = len(result1)
                for i in range (len(result1)):
                    if result1[i]=="where":
                         name_of_insert=result1[i-1]
                         result1.pop(i-1)
                         #temp = temp.replace(name_of_insert," ")
                         break
                for elem in tables:
                    if elem.get_name()==name_of_insert:
                        break
                print(f"this is {elem.get_name()} table")
                #print(name_of_insert)
                temp = temp.replace("where","",1)
               # temp = temp.replace('"'," ")
                result1 = str.split(temp)
                number=0
                size_res=len(result1)
                if '"' in  result1[size_res-1]:
                    temp = temp.replace('"'," ")
                    result1 = str.split(temp)
                    result1.pop(len(result1)-4)
                #print(result1)
                    col_names=[]
                    indexes=[]
                    elem.get_col_name(col_names)
                    size_col_names= len(col_names)
                    size_res= len(result1)
                    number=0
                    size_res=len(result1)
                    for k in range (size_res-2):
                        for i in range (size_col_names):
                            if col_names[i]==result1[k]:
                                indexes.append(i)
                            if col_names[i]==result1[size_res-3]:
                                number=i+1
                    result1.pop(size_res-3)
                    indexes.pop(len(indexes)-1)
                    for i in range (len(indexes)-1):
                        if indexes[i+1]<indexes[i]:
                             raise Exception("wrong order")
                    if len(indexes)<(len(result1)-3):
                        raise Exception("wrong")
                    if number ==0:
                        raise Exception("wrong column")
                    #delete_dupes(indexes)
                    size_res=len(result1)
                    elem.show_col_where(indexes, number-1,result1[size_res-2], result1[size_res-1])
                    EmpInput=""
                    number=0
                    
                    elif '"' in  result1[size_res-3]:
                    temp = temp.replace('"'," ")
                    result1 = str.split(temp)
                    result1.pop(len(result1)-4)
                #print(result1)
                    col_names=[]
                    indexes=[]
                    elem.get_col_name(col_names)
                    size_col_names= len(col_names)
                    size_res= len(result1)
                    number=0
                    size_res=len(result1)
                    for k in range (size_res):
                        for i in range (size_col_names):
                            if col_names[i]==result1[k]:
                                indexes.append(i)
                            if col_names[i]==result1[size_res-1]:
                                number=i+1
                    result1.pop(size_res-1)
                    indexes.pop(len(indexes)-1)
                    for i in range (len(indexes)-1):
                        if indexes[i+1]<indexes[i]:
                             raise Exception("wrong order")
                    if len(indexes)<(len(result1)-3):
                        raise Exception("wrong")
                    if number ==0:
                        raise Exception("wrong column")
                    #delete_dupes(indexes)
                    size_res=len(result1)
                    elem.show_col_where(indexes, number-1,result1[size_res-1], result1[size_res-2])
        
            #except:
             #print("opps")
                """
                EmpInput=""
                number=0
                while ";" not in EmpInput:
                 EmpInput += input()
                 EmpInput+='  '
        else:
            #result1 = re.match(r'select\s+([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\s+from\s+[a-zA-Z0-9]+\s*', EmpInput)
            #temp = result1.group(0)
            s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*'
            if re.match(s1, EmpInput) is not None:
                temp=EmpInput
                temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ', temp)
                temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
                temp = temp.replace("select","",1)
                temp = temp.replace("from","",1)
                temp = temp.replace(" ","",1)
                temp = temp.replace(","," ")
                result1 = str.split(temp) # название таблицы 
                size = len(result1)
                check_if_name_is_right=-1
                for elem in tables:
                    if elem.get_name()==result1[size-1]:
                        name_of_insert= elem.get_name()
                        check_if_name_is_right=1
                        break
                try:
                    if check_if_name_is_right==-1:
                            raise Exception("wrong name")
                    else:
                       
                        result1.pop(size-1)
                        arr=[]
                        indexes=[]
                        elem.get_col_name(arr)
                        size_arr= len(arr)
                        size_res= len(result1)
                        for k in range (size_res):
                            for i in range (size_arr):
                                if arr[i]==result1[k]:
                                    indexes.append(i)
                        try:
                            for i in range (len(indexes)-1):
                                if indexes[i+1]<indexes[i]:
                                     raise Exception("wrong order")
                            if len(indexes)<(len(result1)):
                                raise Exception("wrong")
                            else:
                                try: 
                                    print(f"this is {elem.get_name()} table")
                                    elem.show_col(indexes)
                                except:
                                    print("smth went wrong")
                        except Exception:
                            print("smth went wrong")
                except Exception:
                    print('wrong name')
            EmpInput=""
            while ";" not in EmpInput:
                EmpInput += input()
                EmpInput+='  '
    elif ("delete" in EmpInput1):
        if ("where" in EmpInput1):
            s1= '\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*(\"[^\"]+\"\s*)'
            s2='\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+'
            #result1 = re.match(r'delete\s+from\s+[a-zA-Z0-9]+\s* where\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*("[^"]+"\s*)', EmpInput)
            s3='\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+'
            if re.match(s1, EmpInput) is not None:
                temp = EmpInput
                temp=re.sub(r'(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)','  delete  ', temp)
                temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
                temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ', temp)
                temp = temp.replace("delete","",1)
                temp = temp.replace("from","",1)
                temp = temp.replace(" ","",1)
                temp = temp.replace(","," ")
                temp = temp.replace(";"," ")
                
                if ("<=" in EmpInput):
                     temp = temp.replace("<="," <= ")
                elif (">=" in EmpInput):
                    temp = temp.replace(">="," >=  ")
                elif (">" in EmpInput):
                    temp = temp.replace(">"," > ")
                elif ("<" in EmpInput):
                    temp = temp.replace("<"," <  ")
                elif ("=" in EmpInput):
                    temp = temp.replace("="," =  ")
                result1 = str.split(temp) # название таблицы 
                size = len(result1)
                for i in range (len(result1)):
                    if result1[i]=="where":
                         name_of_insert=result1[i-1]
                         result1.pop(i-1)
                         #temp = temp.replace(name_of_insert," ")
                         break
                check_if_name_is_right=-1
                for elem in tables:
                    if elem.get_name()==name_of_insert:
                        check_if_name_is_right=1
                        break
                try:
                    if check_if_name_is_right==-1:
                        raise Exception("wrong name")
                    else:
                        
                        #print(name_of_insert)
                        temp = temp.replace("where","",1)
                        temp = temp.replace('"'," ")
                        result1 = str.split(temp)
                        result1.pop(len(result1)-4)
                        #print(result1)
                        col_names=[]
                        indexes=[]
                        elem.get_col_name(col_names)
                        size_col_names= len(col_names)
                        size_res= len(result1)
                        number=0
                        for k in range (size_res-2):
                            for i in range (size_col_names):
                                if col_names[i]==result1[size_res-3]:
                                    number=i+1
                        result1.pop(size_res-3)
                        try:
                            if number ==0:
                                raise Exception("wrong column")
                            else:
                                try:
                                    print(f"we deleted rows from {elem.get_name()} table")
                                    size_res=len(result1)
                                    elem.delete_col_where(number-1,result1[size_res-2], result1[size_res-3])
                                except:
                                    print("smth went wrong")
                        except Exception:
                                print('wrong column')
                except Exception:
                    print('wrong name')
            elif re.match(s2, EmpInput) is not None:
                temp = EmpInput
                temp=re.sub(r'(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)','  delete  ', temp)
                temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
                temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ', temp)
                temp = temp.replace("delete","",1)
                temp = temp.replace("from","",1)
                temp = temp.replace(" ","",1)
                temp = temp.replace(","," ")
                temp = temp.replace(";"," ")
                #temp = temp.replace("="," = ",1)
                #temp = temp.replace("<"," < ",1)
                if ("<=" in EmpInput):
                     temp = temp.replace("<="," >= ")
                elif (">=" in EmpInput):
                    temp = temp.replace(">="," <=  ")
                elif (">" in EmpInput):
                    temp = temp.replace(">"," < ")
                elif ("<" in EmpInput):
                    temp = temp.replace("<"," >  ")
                elif ("=" in EmpInput):
                    temp = temp.replace("="," =  ")
                result1 = str.split(temp) # название таблицы 
                size = len(result1)
                for i in range (len(result1)):
                    if result1[i]=="where":
                         name_of_insert=result1[i-1]
                         result1.pop(i-1)
                         #temp = temp.replace(name_of_insert," ")
                         break
                check_if_name_is_right=-1
                for elem in tables:
                    if elem.get_name()==name_of_insert:
                        check_if_name_is_right=1
                        break
                try:
                    if check_if_name_is_right==-1:
                        raise Exception("wrong name")
                    else:
                       
                        #print(name_of_insert)
                        temp = temp.replace("where","",1)
                        temp = temp.replace('"'," ")
                        result1 = str.split(temp)
                        result1.pop(len(result1)-4)
                        #print(result1)
                        col_names=[]
                        indexes=[]
                        elem.get_col_name(col_names)
                        size_col_names= len(col_names)
                        size_res= len(result1)
                        number=0
                        for k in range (size_res):
                            for i in range (size_col_names):
                                if col_names[i]==result1[size_res-1]:
                                    number=i+1
                        result1.pop(size_res-1)
                        try:
                            if number ==0:
                                raise Exception("wrong column")
                            else:
                                try:
                                    print(f"we deleted rows from {elem.get_name()} table")
                                    size_res=len(result1)
                                    elem.delete_col_where(number-1,result1[size_res-3], result1[size_res-2])
                                except:
                                    print("smth went wrong")
                        except Exception:
                            print("wrong column")
                except Exception:
                    print('wrong name')
            elif re.match(s3, EmpInput) is not None:
                temp = EmpInput
                temp=re.sub(r'(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)','  delete  ', temp)
                temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
                temp=re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)','  where  ', temp)
                temp = temp.replace("delete","",1)
                temp = temp.replace("from","",1)
                temp = temp.replace(" ","",1)
                temp = temp.replace(","," ")
                temp = temp.replace(";"," ")
                if ("<=" in EmpInput):
                     temp = temp.replace("<="," <= ")
                elif (">=" in EmpInput):
                    temp = temp.replace(">="," >=  ")
                elif (">" in EmpInput):
                    temp = temp.replace(">"," > ")
                elif ("<" in EmpInput):
                    temp = temp.replace("<"," <  ")
                elif ("=" in EmpInput):
                    temp = temp.replace("="," =  ")
                result1 = str.split(temp) # название таблицы 
                size = len(result1)
                for i in range (len(result1)):
                    if result1[i]=="where":
                         name_of_insert=result1[i-1]
                         result1.pop(i-1)
                         #temp = temp.replace(name_of_insert," ")
                         break
                check_if_name_is_right=-1
                for elem in tables:
                    if elem.get_name()==name_of_insert:
                        check_if_name_is_right=1
                        break
                try:
                    if check_if_name_is_right==-1:
                        raise Exception("wrong name")
                    else:
                        
                        #print(name_of_insert)
                        temp = temp.replace("where","",1)
                        temp = temp.replace('"'," ")
                        result1 = str.split(temp)
                        result1.pop(len(result1)-4)
                        #print(result1)
                        col_names=[]
                        indexes=[]
                        elem.get_col_name(col_names)
                        size_col_names= len(col_names)
                        size_res= len(result1)
                        number1=0
                        number2=0
                        for k in range (size_res-2):
                            for i in range (size_col_names):
                                if col_names[i]==result1[size_res-3]:
                                    number1=i+1
                                if col_names[i]==result1[size_res-1]:
                                    number2=i+1
                        result1.pop(size_res-3)
                        try:
                            if number1 ==0:
                                raise Exception("wrong column")
                            if number2 ==0:
                                raise Exception("wrong column")
                            else:
                                try:
                                    print(f"we deleted rows from {elem.get_name()} table")
                                    size_res=len(result1)
                                    elem.delete_col_where_two_col(number1-1,number2-1, result1[size_res-2])
                                except:
                                   print("smth went wrong")
                        except Exception:
                                print('wrong column')
                except Exception:
                    print('wrong name')
            EmpInput=""
            number=0
            while ";" not in EmpInput:
                EmpInput += input()
                EmpInput+='  '
        else:
            s1='\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*'  
            if re.match(s1, EmpInput) is not None:
            #result1 = re.match(r'delete\s+from\s+[a-zA-Z0-9]+\s*', EmpInput)
                temp = EmpInput
                temp=re.sub(r'(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)','  delete  ', temp)
                temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
                temp = temp.replace("delete","",1)
                temp = temp.replace("from","",1)
                temp = temp.replace(" ","",1)
                temp = temp.replace(","," ")
                temp = temp.replace(";"," ")
                result1 = str.split(temp) # название таблицы 
                for elem in KeyWords:
                    if result1[0]==elem:
                        raise Exception("cant't use key words")
                check_if_name_is_right=-1
                for elem in tables:
                    if elem.get_name()==result1[0]:
                        name_of_insert= elem.get_name()
                        check_if_name_is_right=1
                        break
                try:
                    if check_if_name_is_right==-1:
                        raise Exception("wrong name")
                    else:
                        try:
                            print(f"we deleted everything from {elem.get_name()} table")
                            elem.delete_all()
                        except:
                            print("smth went wrong")
                except Exception: 
                    print('wrong name')
            EmpInput=""
            while ";" not in EmpInput:
                EmpInput += input()
                EmpInput+='  '
    #EmpInput=""
    else:
        EmpInput=""
        while ";" not in EmpInput:
            EmpInput += input()
            EmpInput+='  '
for table in tables:
    print(f"this is {table.get_name()} table")
    table.show()
