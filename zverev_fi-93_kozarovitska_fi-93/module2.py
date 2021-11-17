import re
def assign(arr1, arr2):
    for i in range (len(arr1)):
        arr2.append(arr1[i])
def create_table(EmpInput, result1, index1,number_of_index1):
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
                assign(result, result1)
                assign(index, index1)
                assign(number_of_index, number_of_index1)
                name_table1=name_table
                return name_table
def insert_table(EmpInput, column_values1):
        s1='\s*(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)\s+[a-zA-Z0-9]+\s*\(\s*("[^"]+"\s*,\s*)*("[^"]+"\s*)\)\s*'
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
            name_of_table= result1[0]
            assign(column_values, column_values1)
            return name_of_table
def select_all_where(EmpInput, result):
    s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*(w|W)(h|H)(e|E)(r|R)(e|E)\s+([a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*(\"[^\"]+\"\s*))'
    s2='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) \s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
    s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) \s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
    if (re.match(s1, EmpInput) is not None) or (re.match(s2, EmpInput) is not None) or (re.match(s3, EmpInput) is not None):
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
                    name_of_table=result1[i-1]
                    result1.pop(i-1)
                    break
        temp = temp.replace("where","",1)
        temp = temp.replace('"'," ")
        size_res=len(result1)
        result1 = str.split(temp)
        result1.pop(len(result1)-4)
        size_res=len(result1)
        if re.match(s1, EmpInput) is not None:
            value=re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"',"")
            result.append(result1[size_res-3])
            result.append(result1[size_res-2])
            result.append(value)
        if re.match(s2, EmpInput) is not None:
            if result1[size_res-2]=='<=':
                result1[size_res-2]='>='
            elif result1[size_res-2]=='>=':
                result1[size_res-2]='<='
            elif result1[size_res-2]=='>':
                result1[size_res-2]='<'
            elif result1[size_res-2]=='<':
                result1[size_res-2]='>'
            value=re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"',"")
            result.append(result1[size_res-1])
            result.append(result1[size_res-2])
            result.append(value)
        if re.match(s3, EmpInput) is not None:
            result.append(result1[size_res-3])
            result.append(result1[size_res-2])
            result.append(result1[size_res-1])
        return name_of_table
def select_all(EmpInput):
    s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*'
    if re.match(s1, EmpInput) is not None:
        temp = EmpInput
        temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ',  temp)
        temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ',  temp)
        temp = temp.replace("select","",1)
        temp = temp.replace("from","",1)
        temp = temp.replace(" ","",1)
        temp = temp.replace(","," ")
        temp = temp.replace(";"," ")
        result1 = str.split(temp)
        name_table= result1[1]
        return name_table
def select_where(EmpInput, result):
    result1=[]
    s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*("[^"]+"\s*)'
    s2='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) ([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+("[^"]+"\s*)((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
    s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) ([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+\s*'
    if (re.match(s1, EmpInput) is not None) or (re.match(s2, EmpInput) is not None) or (re.match(s3, EmpInput) is not None):
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
        temp = temp.replace("where","",1)
                           # temp = temp.replace('"'," ")
        number=0
        
        temp = temp.replace('"'," ")
        result1 = str.split(temp)
        result1.pop(len(result1)-4)
        size_res=len(result1)
        if re.match(s1, EmpInput) is not None:
            result1.pop(len(result1)-1)
            value=re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"',"")
            result1.append(value)
            assign(result1, result)
        elif re.match(s2, EmpInput) is not None:
            if result1[size_res-2]=='<=':
                result1[size_res-2]='>='
            elif result1[size_res-2]=='>=':
                result1[size_res-2]='<='
            elif result1[size_res-2]=='>':
                result1[size_res-2]='<'
            elif result1[size_res-2]=='<':
                result1[size_res-2]='>'
            result1[size_res-3], result1[size_res-1]=result1[size_res-1], result1[size_res-3]
            result1.pop(len(result1)-1)
            value=re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"',"")
            result1.append(value)
            assign(result1, result)
        elif re.match(s3, EmpInput) is not None:
            assign(result1, result)
        return name_of_insert
def select_columns(EmpInput, result):
    s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*'
    if re.match(s1, EmpInput) is not None:
        temp=EmpInput
        temp=re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)','  select  ', temp)
        temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
        temp = temp.replace("select","",1)
        temp = temp.replace("from","",1)
        temp = temp.replace(" ","",1)
        temp = temp.replace(","," ")
        #temp=temp[:-1]
        #temp = temp.replace(";","",1)
        result1 = str.split(temp) # название таблицы 
        size = len(result1)
        assign(result1, result)
        name_of_insert=result1[size-1]
        name_of_insert =  name_of_insert.replace(";","",1)
        return name_of_insert
def delete_where(EmpInput, result):
    s1= '\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*(\"[^\"]+\"\s*)'
    s2='\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+'
    s3='\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=))\s*[a-zA-Z0-9]+'
    if (re.match(s1, EmpInput) is not None) or (re.match(s2, EmpInput) is not None) or (re.match(s3, EmpInput) is not None):
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
                    break
        temp = temp.replace("where","",1)
        temp = temp.replace('"'," ")
        result1 = str.split(temp)
        result1.pop(len(result1)-4)
        size_res = len(result1)
        if re.match(s1, EmpInput) is not None:
                result1.pop(len(result1)-1)
                value=re.findall(r'\"[^\"]+\"', EmpInput)
                value = value[0].replace('"',"")
                result1.append(value)
                assign(result1, result)
        elif re.match(s2, EmpInput) is not None:
            if result1[size_res-2]=='<=':
                result1[size_res-2]='>='
            elif result1[size_res-2]=='>=':
                result1[size_res-2]='<='
            elif result1[size_res-2]=='>':
                result1[size_res-2]='<'
            elif result1[size_res-2]=='<':
                result1[size_res-2]='>'
            result1[size_res-3], result1[size_res-1]=result1[size_res-1], result1[size_res-3]
            result1.pop(len(result1)-1)
            value=re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"',"")
            result1.append(value)
            assign(result1, result)
        elif re.match(s3, EmpInput) is not None:
            assign(result1, result)
        return name_of_insert
def delete(EmpInput):
    s1='\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*'  
    if re.match(s1, EmpInput) is not None:
        temp = EmpInput
        temp=re.sub(r'(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)','  delete  ', temp)
        temp=re.sub(r'(f|F)(r|R)(o|O)(M|m)','  from  ', temp)
        temp = temp.replace("delete","",1)
        temp = temp.replace("from","",1)
        temp = temp.replace(" ","",1)
        temp = temp.replace(","," ")
        temp = temp.replace(";"," ")
        result1 = str.split(temp) # название таблицы 
        name_of_insert=result1[0]
        return name_of_insert
            
