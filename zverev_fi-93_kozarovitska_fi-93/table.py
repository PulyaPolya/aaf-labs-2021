import tree
import parsing


def delete(column_names, columns, right_rows):
    size = len(column_names)
    size_col = len(columns[0])
    indexes_of_right_col = []
    for i in range(len(column_names)):
        indexes_of_right_col.append(i)
    for j in reversed(right_rows):
        for i in reversed(indexes_of_right_col):
            # columns[i][j]="*"
            if columns[i]:
                columns[i].pop(j)


def delete_dupes(arr):
    size = len(arr)
    for i in range(1, size):
        if i >= size:
            break
        if arr[i] == arr[i - 1]:
            arr.pop(i)
            size = len(arr)
    size = len(arr)
    if size > 2:
        if (arr[size - 1] == arr[size - 2]):
            arr.pop(size - 1)


def delete_dupes_rand_order(arr):
    arr1 = []
    for i in reversed(arr):
        if i not in arr1:
            arr1.append(i)
    arr1.sort()
    arr = []
    for elem in arr1:
        arr.append(elem)
    return arr


def edit_arr(arr):
    delete_dupes(arr)
    arr.sort()


def beatiful_print(column_names, columns, indexes_of_right_col, right_rows):
    if not right_rows:
        print("selection is empty")
    else:
        size = len(column_names)
        size_col = len(columns[0])
        max = []
        for i in range(size):
            max.append(len(column_names[i]))

        print('\n')
        for j in right_rows:
            for i in indexes_of_right_col:
                if len(columns[i][j]) > max[i]:
                    max[i] = len(columns[i][j])
        # print(max)

        for i in indexes_of_right_col:
            t = max[i] - len(column_names[i])
            if (t % 2 == 0):
                print("|", end='')
                k = 0
                while k < t / 2:
                    print(" ", end='')
                    k = k + 1
                print(column_names[i], end='')
                k = 0
                while k < t / 2:
                    print(" ", end='')
                    k = k + 1

            else:
                print("|", end='')
                k = 0
                while k < t / 2 - 1:
                    print(" ", end='')
                    k = k + 1
                print(column_names[i], end='')
                k = 0
                while k < t / 2:
                    print(" ", end='')
                    k = k + 1
        print("|", end='')
        print('\n')
        print("+", end='')
        for i in indexes_of_right_col:
            k = 0
            while k < max[i]:
                print("-", end='')
                k = k + 1
            print("+", end='')
        print('\n')
        for j in right_rows:
            for i in indexes_of_right_col:
                t = max[i] - len(columns[i][j])
                if (t % 2 == 0):
                    print("|", end='')
                    k = 0
                    while k < t / 2:
                        print(" ", end='')
                        k = k + 1
                    print(columns[i][j], end='')
                    k = 0
                    while k < t / 2:
                        print(" ", end='')
                        k = k + 1

                else:
                    print("|", end='')
                    k = 0
                    while k < t / 2 - 1:
                        print(" ", end='')
                        k = k + 1
                    print(columns[i][j], end='')
                    k = 0
                    while k < t / 2:
                        print(" ", end='')
                        k = k + 1
            print("|", end='')
            print('\n')
        print("+", end='')
        for i in indexes_of_right_col:
            k = 0
            while k < max[i]:
                print("-", end='')
                k = k + 1
            print("+", end='')
        print('\n')


class Table:
    size_table = 0
    size_indexed = 0

    def __init__(self, name, result, indexed, number_of_index):
        self.name = name
        self.numb_of_rows = 0
        self.number = []
        self.column_names = []
        self.columns = []
        self.indexed = []
        self.name_of_indexed = []
        self.number_of_index = []
        self.del_all = 1
        self.size_indexed = len(indexed)
        for k in range(self.size_indexed):
            self.indexed.append(indexed[k])
            self.name_of_indexed.append(indexed[k])
            self.number_of_index.append(number_of_index[k])
        size = len(result)
        self.size_table = len(result)
        for i in range(size):
            self.columns.append(result[i])
            self.column_names.append(result[i])
            self.columns[i] = []

    def add_row(self, number, result):
        if (len(self.number) == 0):
            n = 1
        else:
            n = max(self.number) + 1
        self.number.append(n)
        # print(f"this is self.number {self.number}")
        size = len(self.column_names)
        size_col = len(self.columns[0])
        for i in range(size):
            self.columns[i].append(result[i])
        if self.numb_of_rows == 0:
            for k in range(self.size_indexed):
                temp1 = self.number_of_index[k]  ####
                # print(result[temp1])
                self.indexed[k] = tree.newNode(result[temp1], 0)
        elif self.numb_of_rows != 0:
            for k in range(self.size_indexed):
                temp1 = self.number_of_index[k]
                # print(result[temp1])
                self.indexed[k] = tree.insert(self.indexed[k], result[temp1], n - 1)
        self.numb_of_rows = self.numb_of_rows + 1

    def get_name(self):
        return self.name

    def get_numb_of_rows(self):
        return self.numb_of_rows

    def get_table(self):
        return self.columns

    def get_col_name(self, arr):
        for i in range(self.size_table):
            arr.append(self.column_names[i])

    def get_size(self):
        return self.size_table

    def show(self, indexes_of_right_col1, right_rows1):
        indexes_of_right_col = []
        right_rows = []
        size_col = len(self.columns[0])
        for t in range(size_col):
            right_rows.append(t)
        for i in range(len(self.column_names)):
            indexes_of_right_col.append(i)
        parsing.assign(indexes_of_right_col, indexes_of_right_col1)
        parsing.assign(right_rows, right_rows1)
        # beatiful_print(self.column_names, self.columns,indexes_of_right_col,right_rows)#!!!!

    def delete_all(self):
        indexes_of_right_col = []
        self.number = []
        self.numb_of_rows = 0
        right_rows = []
        self.del_all = 0
        for t in range(len(self.indexed)):
            self.indexed[t] = tree.deleteAll(self.indexed[t])
        self.indexed = []
        parsing.assign(self.name_of_indexed, self.indexed)
        size_col = len(self.columns[0])
        for t in range(size_col):
            right_rows.append(t)
        for i in range(len(self.column_names)):
            indexes_of_right_col.append(i)
        delete(self.column_names, self.columns, right_rows)

    def show_col(self, indexes_of_right_col, right_rows1):
        right_rows = []
        size_col = len(self.columns[0])
        for t in range(size_col):
            right_rows.append(t)
        parsing.assign(right_rows, right_rows1)
        # beatiful_print(self.column_names, self.columns, indexes_of_right_col,right_rows)

    def show_col_where(self, col_mumbers, number, symbol, value, right_arr_rows1):
        size = len(self.column_names)
        size_col = len(self.columns[0])
        numb_of_rows = []
        numb = -1  # number column, which is indexed and in which we need to find value
        for t in range(len(self.number_of_index)):
            if number == self.number_of_index[t]:
                numb = t
                break
        if numb >= 0:  # that means that we found smth indexed
            right_rows = []  # array for number of indexed columns, which we need to print
            right_arr_rows = []
            res_temp = []
            if (symbol == "="):
                tree.find(self.indexed[t], value, right_rows)
            elif (symbol == "<"):
                tree.find_l(self.indexed[t], value, right_rows)
            elif (symbol == "<="):
                tree.find_l_eq(self.indexed[t], value, right_rows)
            elif (symbol == ">"):
                tree.find_g(self.indexed[t], value, right_rows)
            elif (symbol == ">="):
                tree.find_g_eq(self.indexed[t], value, right_rows)
            for j in right_rows:
                for k in range(len(self.number)):
                    if j + 1 == self.number[k]:
                        right_arr_rows.append(k)
            # beatiful_print(self.column_names,self.columns,col_mumbers, right_arr_rows)
        else:
            res_temp = []
            right_rows = []
            right_arr_rows = []
            if (symbol == "="):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] == value:
                        right_rows.append(k)
            elif (symbol == "<"):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] < value:
                        right_rows.append(k)
            elif (symbol == "<="):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] <= value:
                        right_rows.append(k)
            elif (symbol == ">"):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] > value:
                        right_rows.append(k)
            elif (symbol == ">="):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] >= value:
                        right_rows.append(k)
            parsing.assign(right_rows, right_arr_rows)
        parsing.assign(right_arr_rows, right_arr_rows1)
        # beatiful_print(self.column_names,self.columns,col_mumbers, right_rows)

    def show_col_where_two_col(self, col_mumbers, number1, number2, symbol, right_rows1):
        right_rows = []
        if (symbol == "="):
            for k in range(len(self.columns[0])):
                if self.columns[number1][k] == self.columns[number2][k]:
                    right_rows.append(k)
        elif (symbol == "<"):
            for k in range(len(self.columns[number1])):
                if self.columns[number1][k] < self.columns[number2][k]:
                    right_rows.append(k)
        elif (symbol == "<="):
            for k in range(len(self.columns[number1])):
                if self.columns[number1][k] <= self.columns[number2][k]:
                    right_rows.append(k)
        elif (symbol == ">"):
            for k in range(len(self.columns[number1])):
                if self.columns[number1][k] > self.columns[number2][k]:
                    right_rows.append(k)
        elif (symbol == ">="):
            for k in range(len(self.columns[number1])):
                if self.columns[number1][k] >= self.columns[number2][k]:
                    right_rows.append(k)
        parsing.assign(right_rows, right_rows1)
        # beatiful_print(self.column_names,self.columns,col_mumbers, right_rows)

    def delete_col_where(self, number, symbol, value):
        size = len(self.column_names)
        size_col = len(self.columns[0])
        numb_of_rows = []
        numb = -1  # number column, which is indexed and in which we need to find value
        for t in range(len(self.number_of_index)):
            if number == self.number_of_index[t]:
                numb = t
                break
        if numb >= 0:  # that means that we found smth indexed
            right_rows = []  # array for number of indexed columns, which we need to print
            key_values = []#!!!
            right_arr_rows = []
            if (symbol == "="):
                tree.find(self.indexed[t], value, right_rows)  # finds numbers of value in tree

                        #if i == len(right_rows):
                           # break
            elif (symbol == "<"):
                tree.find_l(self.indexed[t], value, right_rows)
            elif (symbol == "<="):
                tree.find_l_eq(self.indexed[t], value, right_rows)
            elif (symbol == ">"):
                tree.find_g(self.indexed[t], value, right_rows)
            elif (symbol == ">="):
                tree.find_g_eq(self.indexed[t], value, right_rows)
            for j in right_rows:
                for k in range(len(self.number)):
                    if j + 1 == self.number[k]:
                        right_arr_rows.append(k)
            # tree.deleteNode(self.indexed[t], value)
            values_from_other_ind_col = []
            for i in self.number_of_index:
                # if i!=number:
                print(self.columns[i])
            for i in right_arr_rows:
                # if j != number:
                for j in self.number_of_index:
                    # print(self.columns[j][i])
                    values_from_other_ind_col.append(self.columns[j][i])
            i = 0
            j = 0
            for e in range(len(right_rows)):
                # i=0
                for q in range(len(self.indexed)):
                    #tree.inorder(self.indexed[q])
                    self.indexed[q] = tree.deleteNode_number(self.indexed[q], values_from_other_ind_col[i],
                                                             right_rows[e])
                    #print('\n')
                    #tree.inorder(self.indexed[q])
                    #print('\n')
                    #print(values_from_other_ind_col[i], right_rows[e])
                    i = i + 1
            for m in right_rows:
                self.number.remove(m + 1)
            for m in right_arr_rows:
                self.numb_of_rows = self.numb_of_rows - 1
            delete(self.column_names, self.columns, right_arr_rows)
        else:
            right_rows = []
            if (symbol == "="):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] == value:
                        right_rows.append(k)
            elif (symbol == "<"):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] < value:
                        right_rows.append(k)
            elif (symbol == "<="):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] <= value:
                        right_rows.append(k)
            elif (symbol == ">"):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] > value:
                        right_rows.append(k)
            elif (symbol == ">="):
                for k in range(len(self.columns[number])):
                    if self.columns[number][k] >= value:
                        right_rows.append(k)
            for m in right_rows:
                self.number.remove(m + 1)
            for m in right_rows:
                self.numb_of_rows = self.numb_of_rows - 1
            delete(self.column_names, self.columns, right_rows)

    def delete_col_where_two_col(self, number1, number2, symbol):
        key_values = []
        right_rows = []
        if (symbol == "="):
            # find(self.indexed[t], value, right_rows) # finds numbers of value in tree
            for k in range(len(self.columns[0])):
                if self.columns[number1][k] == self.columns[number2][k]:
                    right_rows.append(k)
                    value = self.columns[number1][k]
            for t in range(len(self.number_of_index)):
                if number1 == self.number_of_index[t]:
                    tree.deleteNode(self.indexed[t], value)
            for t in range(len(self.number_of_index)):
                if number2 == self.number_of_index[t]:
                    tree.deleteNode(self.indexed[t], value)
        else:
            if (symbol == "<"):
                values1 = []
                values2 = []
                for k in range(len(self.columns[0])):
                    if self.columns[number1][k] < self.columns[number2][k]:
                        right_rows.append(k)
                        values1.append(self.columns[number1][k])
                        values2.append(self.columns[number2][k])

            elif (symbol == "<="):
                values1 = []
                values2 = []
                for k in range(len(self.columns[0])):
                    if self.columns[number1][k] <= self.columns[number2][k]:
                        right_rows.append(k)
                        values1.append(self.columns[number1][k])
                        values2.append(self.columns[number2][k])
            elif (symbol == ">"):
                values1 = []
                values2 = []
                for k in range(len(self.columns[0])):
                    if self.columns[number1][k] > self.columns[number2][k]:
                        right_rows.append(k)
                        values1.append(self.columns[number1][k])
                        values2.append(self.columns[number2][k])
            elif (symbol == ">="):
                values1 = []
                values2 = []
                for k in range(len(self.columns[0])):
                    if self.columns[number1][k] >= self.columns[number2][k]:
                        right_rows.append(k)
                        values1.append(self.columns[number1][k])
                        values2.append(self.columns[number2][k])
            for t in range(len(self.number_of_index)):
                if number1 == self.number_of_index[t]:
                    for value in values1:
                        tree.deleteNode(self.indexed[t], value)
            for t in range(len(self.number_of_index)):
                if number2 == self.number_of_index[t]:
                    for value in values1:
                        tree.deleteNode(self.indexed[t], value)
        for m in right_rows:
            self.numb_of_rows = self.numb_of_rows - 1
        for m in right_rows:
            self.number.remove(m + 1)
        delete(self.column_names, self.columns, right_rows)
