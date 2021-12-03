import re


def assign(arr1, arr2):
    for i in range(len(arr1)):
        arr2.append(arr1[i])


def create_table(EmpInput, result1, index1, number_of_index1):
    s1 = '\s*(C|c)(r|R)(e|E)(A|a)(t|T)(e|E)\s+[a-zA-Z][a-zA-Z0-9]*\s*\(\s*([a-zA-Z0-9]+\s*((I|i)(N|n)(D|d)(E|e)(X|x)(e|E)(D|d)\s*)*\s*)\s*(\s*,\s*[a-zA-Z0-9]+\s*(\s+(I|i)(N|n)(D|d)(E|e)(X|x)(e|E)(D|d))*)*\s*\)\s*;'
    if re.match(s1, EmpInput) is not None:
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        temp = re.sub(r'(C|c)(r|R)(e|E)(A|a)(t|T)(e|E)', ' create ', EmpInput)
        temp = re.sub(r'(I|i)(N|n)(D|d)(E|e)(X|x)(e|E)(D|d)', 'indexed', temp)
        temp = temp.replace(first_command, "", 1)
        temp = temp.replace("(", " ")
        temp = temp.replace(")", " ")
        temp = temp.replace(" ", "", 1)
        temp = temp.replace(",", " ")
        temp = temp.replace(";", " ")
        #while temp[-1]!=';':
            #temp = temp[:-1]
        #temp = temp[:-1]
        result = str.split(temp)  # название таблицы re.split(r" ", temp)

        name_table = result[0]
        index = []
        number_of_index = []
        size = len(result)
        i = 0
        while i < size:
            if result[i] == "indexed":
                index.append(result[i - 1])
                number_of_index.append(i - 2)
                result.pop(i)
                size = len(result)
            i = i + 1
        result.pop(0)
        assign(result, result1)
        assign(index, index1)
        assign(number_of_index, number_of_index1)
        return name_table


def insert_table(EmpInput, column_values1):
    s1 = '\s*(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)\s+[a-zA-Z0-9]+\s*\(\s*("[^"]+"\s*,\s*)*("[^"]+"\s*)\)\s*;\s*'
    if re.match(s1, EmpInput) is not None:
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        temp1 = re.findall(r'\"[^\"]+\"', EmpInput)
        column_values = []
        temp = re.sub(r'(I|i)(N|n)(S|s)(E|e)(R|r)(T|t)', '  insert  ', EmpInput)
        for elem in temp1:
            elem = elem.replace('"', '')
            column_values.append(elem)
        temp = temp.replace('"', '')
        temp = temp.replace(first_command, "", 1)  # ''
        temp = temp.replace("(", " ")
        temp = temp.replace(")", "")
        temp = temp.replace(";", "")
        temp = temp.replace(" ", "", 1)
        temp = temp.replace(",", " ")
        result1 = str.split(temp)  # название таблицы
        name_of_table = result1[0]
        assign(column_values, column_values1)
        return name_of_table


def replace_value(EmpInput):
    temp = EmpInput
    if ("<=" in EmpInput):
        temp = temp.replace("<=", " <= ", 1)
    elif ("=<" in EmpInput):
        temp = temp.replace("=<", " <= ", 1)
    elif (">=" in EmpInput):
        temp = temp.replace(">=", " >=  ", 1)
    elif ("=>" in EmpInput):
        temp = temp.replace("=>", " >=  ", 1)
    elif ("!=" in EmpInput):
        temp = temp.replace("!=", " !=  ", 1)
    elif (">" in EmpInput):
        temp = temp.replace(">", " > ", 1)
    elif ("<" in EmpInput):
        temp = temp.replace("<", " <  ", 1)
    elif ("=" in EmpInput):
        temp = temp.replace("=", " =  ", 1)

    return temp
def replace_value_reversed(EmpInput):
    temp = EmpInput
    if ("<=" in EmpInput):
        temp = temp.replace("<=", " >= ", 1)
    elif ("=<" in EmpInput):
        temp = temp.replace("=<", " >= ", 1)
    elif (">=" in EmpInput):
        temp = temp.replace(">=", " <=  ", 1)
    elif ("=>" in EmpInput):
        temp = temp.replace("=>", " <=  ", 1)
    elif ("!=" in EmpInput):
        temp = temp.replace("!=", " !=  ", 1)
    elif (">" in EmpInput):
        temp = temp.replace(">", " < ", 1)
    elif ("<" in EmpInput):
        temp = temp.replace("<", " >  ", 1)
    elif ("=" in EmpInput):
        temp = temp.replace("=", " =  ", 1)

    return temp
def select_columns_where(EmpInput, result):

    #s1 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,{0,1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<))\s*("[^"]+"\s*)\s*;'
    s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*)+\s*(\s*,\s*[a-zA-Z0-9]+\s*)*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*(\"[^\"]+\"\s*)\s*;'
    #s2 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) ([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+("[^"]+"\s*)((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<))\s*[a-zA-Z0-9]+\s*;'
    s2='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) ([a-zA-Z0-9]+\s*)+\s*(\s*,\s*[a-zA-Z0-9]+)*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+("[^"]+"\s*)((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    #s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s*([a-zA-Z0-9]+\s*,{1}\s*)*\s*[a-zA-Z0-9]+\s*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*(w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<))\s*[a-zA-Z0-9]+\s*;'
    s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s*([a-zA-Z0-9]+\s*)+\s*(\s*,\s*[a-zA-Z0-9]+)*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*(w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    case=0
    if '"' in EmpInput:
        if re.match(s1, EmpInput) is not None:
            case=1
        if re.match(s2, EmpInput) is not None:
            case=2
    elif re.match(s3, EmpInput) is not None:
        case = 3
    if case!=0:
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        if case==1 or case==3:
            temp = replace_value(EmpInput)
        elif case==2:
            temp=replace_value_reversed(EmpInput)
        temp = re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)', '  select  ', temp)
        temp = re.sub(r'(f|F)(r|R)(o|O)(M|m)', '  from  ', temp)
        temp = re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)', '  where  ', temp)
        temp = temp.replace(first_command, "", 1)
        temp = temp.replace(";", "", 1)
        temp = temp.replace("from", "", 1)
        temp = temp.replace(",", " ")
        result1 = str.split(temp)
        for i in range(len(result1)):
            if result1[i] == "where":
                name_of_insert = result1[i - 1]
                result1.pop(i - 1)
                break
        temp = temp.replace("where", "", 1)
        temp = temp.replace('"', " ")
        result1 = str.split(temp)
        result1.pop(len(result1) - 4)
        size_res = len(result1)
        if case==1:
            result1.pop(len(result1) - 1)
            value = re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"', "")
            result1.append(value)
            assign(result1, result)
            return (name_of_insert, "select col where ''")
        elif case==2:
            result1[size_res - 3], result1[size_res - 1] = result1[size_res - 1], result1[size_res - 3]
            result1.pop(len(result1) - 1)
            value = re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"', "")
            result1.append(value)
            assign(result1, result)
            return (name_of_insert, "select col where ''")
        elif case==3:
            assign(result1, result)
            return (name_of_insert, "select col where two col")



def select_columns(EmpInput, result):

    s1 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*)*(\s*,\s*[a-zA-Z0-9]+\s*)*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*;'
    if re.match(s1, EmpInput) is not None:
        temp = EmpInput
        EmpInput = EmpInput.replace(";", "", 1)
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        temp = re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)', '  select  ', temp)
        temp = re.sub(r'(f|F)(r|R)(o|O)(M|m)', '  from  ', temp)
        temp = temp.replace( first_command, "", 1)
        temp = temp.replace("from", "", 1)
        temp = temp.replace(" ", "", 1)
        temp = temp.replace(",", " ")
        result1 = str.split(temp)  # название таблицы
        size = len(result1)
        assign(result1, result)
        name_of_insert = result1[size - 1]
        name_of_insert = name_of_insert.replace(";", "", 1)
        return name_of_insert

def command_all_where(EmpInput, result):
    s1 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*(w|W)(h|H)(e|E)(r|R)(e|E)\s+([a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*(\"[^\"]+\"\s*))\s*;'
    s2 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) \s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*\s*;'
    s3 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t) \s*\*\s*(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    s4 = '\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*(\"[^\"]+\"\s*)\s*;'
    s5 = '\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    s6 = '\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    case=0
    if re.match(s1, EmpInput) is not None:
        case=1
    if re.match(s2, EmpInput) is not None:
        case=2
    if re.match(s3, EmpInput) is not None:
        case=3
    if re.match(s4, EmpInput) is not None:
        case=4
    if re.match(s5, EmpInput) is not None:
        case=5
    if re.match(s6, EmpInput) is not None:
        case = 6
    if case!=0:
        temp = EmpInput
        if case==1 or case==4:
            temp = replace_value(EmpInput)
        elif case==2 or case==5:
            temp = replace_value_reversed(EmpInput)
        elif case==3 or case==6:
            temp = replace_value(EmpInput)
        #EmpInput = EmpInput.replace(";", "", 1)
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        temp = re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)', '  select  ', temp)
        temp = re.sub(r'(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)', '  delete  ', temp)
        temp = re.sub(r'(f|F)(r|R)(o|O)(M|m)', '  from  ', temp)
        temp = re.sub(r'(w|W)(h|H)(e|E)(r|R)(e|E)', '  where  ', temp)
        temp = temp.replace(first_command, "", 1)
        #temp = temp.replace("delete", "", 1)
        temp = temp.replace(";", "", 1)
        temp = temp.replace("from", "", 1)
        temp = temp.replace(" ", "", 1)
        temp = temp.replace(",", " ")
        result1 = str.split(temp)  # название таблицы
        for i in range(len(result1)):
            if result1[i] == "where":
                name_of_table = result1[i - 1]
                result1.pop(i - 1)
                break
        temp = temp.replace("where", "", 1)
        temp = temp.replace('"', " ")
        result1 = str.split(temp)
        result1.pop(len(result1) - 4)
        size_res = len(result1)
        if case==1 or case==4:
            value = re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"', "")
            result.append(result1[size_res - 3])
            result.append(result1[size_res - 2])
            result.append(value)
        elif case==2 or case==5:
            value = re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"', "")
            result.append(result1[size_res - 1])
            result.append(result1[size_res - 2])
            result.append(value)
        elif case==3 or case==6:
            result.append(result1[size_res - 3])
            result.append(result1[size_res - 2])
            result.append(result1[size_res - 1])
        if case==1 or case==2: #re.match(s1, EmpInput) is not None or  re.match(s2, EmpInput) is not None
            return(name_of_table, "select where ''")
        if case==3: #re.match(s3, EmpInput) is not None
            return (name_of_table, "select where two col")
        if case==4 or case==5: #re.match(s4, EmpInput) is not None or re.match(s5, EmpInput) is not None
            return (name_of_table, "delete where ''")
        if case==6: # re.match(s6, EmpInput) is not None
            return (name_of_table, "delete where two col")
        #return name_of_table

def command_all(EmpInput):
    s1 = '\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*;'
    s2 = '\s*(D|d)(e|E)(l|L)(e|E)(T|t)(E|e)\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s*;'
    case=0
    if re.match(s1, EmpInput) is not None:
        case = 1
    if re.match(s2, EmpInput) is not None:
        case = 2
    if case!=0:
        temp = EmpInput
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        temp = re.sub(r'(f|F)(r|R)(o|O)(M|m)', '  from  ', temp)
        temp = temp.replace(first_command, "", 1)
        temp = temp.replace("from", "", 1)
        temp = temp.replace(" ", "", 1)
        temp = temp.replace(",", " ")
        temp = temp.replace(";", " ")
        result1 = str.split(temp)
        if case==1: #re.match(s1, EmpInput) is not None
            name_table = result1[1]
            return (name_table, "select")
        else:
            name_table = result1[0]
            return (name_table, "delete")

def exit(EmpInput):
    s1= '\s*(e|E)(x|X)(i|I)(t|T)\s*;'
    if re.match(s1, EmpInput) is not None:
        return 1


def full_join(EmpInput):
    s1='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,\s*)*\s*[a-zA-Z0-9]+\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*=\s*[a-zA-Z0-9]+;'
    s2='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,\s*)*\s*[a-zA-Z0-9]+\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s+(w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*("[^"]+"\s*)\s*;'
    s3='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,\s*)*\s*[a-zA-Z0-9]+\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s+(w|W)(h|H)(e|E)(r|R)(e|E)\s+("[^"]+"\s*)((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    s4='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+([a-zA-Z0-9]+\s*,\s*)*\s*[a-zA-Z0-9]+\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s+(w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    s5='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*=\s*[a-zA-Z0-9]+;'
    s6='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<))\s*[a-zA-Z0-9]+\s+(w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*(\"[^\"]+\"\s*)\s*;'
    s7='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<))\s*[a-zA-Z0-9]+\s+(w|W)(h|H)(e|E)(r|R)(e|E)\s+(\"[^\"]+\"\s*)((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    s8='\s*(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)\s+\*\s+(f|F)(r|R)(o|O)(M|m)\s+[a-zA-Z0-9]+\s* (F|f)(u|U)(L|l)(L|l)\s+(J|j)(O|o)(I|i)(N|n)\s+[a-zA-Z0-9]+\s+(O|o)(N|n)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<))\s*[a-zA-Z0-9]+\s+(w|W)(h|H)(e|E)(r|R)(e|E)\s+[a-zA-Z0-9]+\s*((=)||(<=)||(<)||(>)||(>=)||(=>)||(=<)||(!=))\s*[a-zA-Z0-9]+\s*;'
    case=0
    if re.match(s1, EmpInput) is not None:
            case=1
    elif re.match(s2, EmpInput) is not None:
        case=2
    elif re.match(s3, EmpInput) is not None:
        case =3
    elif re.match(s4, EmpInput) is not None:
        case = 4
    elif re.match(s5, EmpInput) is not None:
        case = 5
    elif re.match(s6, EmpInput) is not None:
        case = 6
    elif re.match(s7, EmpInput) is not None:
        case = 7
    elif re.match(s8, EmpInput) is not None:
        case = 8
    if case!=0:
        temp = EmpInput
        EmpInput1 = EmpInput.casefold()
        first_command = EmpInput1.split()[0]
        if case==2 or case==4 or case==6 or case ==8:
            temp = replace_value(EmpInput)
        elif case==3 or case==7:
            temp=replace_value_reversed(EmpInput)
        temp = re.sub(r'(S|s)(e|E)(L|l)(E|e)(c|C)(T|t)', '  select  ', temp)
        temp = re.sub(r'(f|F)(r|R)(o|O)(M|m)', '  from  ', temp)
        temp = re.sub(r'(F|f)(u|U)(L|l)(L|l)', '  full  ', temp)
        temp = re.sub(r'(J|j)(O|o)(I|i)(N|n)', '  join  ', temp)
        temp = re.sub(r'(O|o)(N|n)', '  on  ', temp)
        temp = re.sub(r'=', '  =  ', temp, 1)
        temp = re.sub(r';', '  ', temp)
        temp = temp.replace(first_command, "", 1)
        temp = temp.replace(" ", "", 1)
        temp = temp.replace(",", " ")
        result1 = str.split(temp)
        col_names=[]
        for a in range (len(result1)):
            if result1[a]=='from':
                break
        if case<5:
            for t in range(a):
                col_names.append(result1[t])
        table1=result1[a+1]
        for b in range (len(result1)):
            if result1[b]=='join':
                break
        table2=result1[b+1]
        size=len(result1)
        #symbol='='

        if case==2 or case==3 or case==6 or case== 7:
            value = re.findall(r'\"[^\"]+\"', EmpInput)
            value = value[0].replace('"', "")
            col2 = result1[size - 5]
            col1 = result1[size - 7]
            symbol=result1[size - 2]
            if case==2 or case ==6:
                col_to_compare = result1[size - 3]
            else:
                col_to_compare = result1[size - 1]
            if case== 2 or case==3:
                return (col_names, table1, table2, col1, col2, 'full join where "" ', col_to_compare, value, symbol)
            else:
                return (None, table1, table2, col1, col2, '* full join where "" ', col_to_compare, value, symbol)
        elif case==4 or case== 8:
            col2 = result1[size - 5]
            col1 = result1[size - 7]
            col_to_compare2 = result1[size - 1]
            col_to_compare1 = result1[size - 3]
            symbol = result1[size - 2]
            if case== 4:
                return (col_names, table1, table2, col1, col2, "full join where two col", col_to_compare1, col_to_compare2, symbol)
            else:
                return (None, table1, table2, col1, col2, "* full join where two col", col_to_compare1, col_to_compare2, symbol)
        else:
            col1 = result1[size - 3]
            col2 = result1[size - 1]
            if case== 1:
                return(col_names, table1, table2,col1, col2, "full join" )
            else:
                return (None, table1, table2, col1, col2, "* full join")
    else:
        return None
