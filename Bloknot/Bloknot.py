import os
from datetime import datetime


def wwod():
    vw = input()
    return vw

# wwod
# print(wwod(), datetime.now())
# ##print()
# ##def ident():
def datenow():
    fd = datetime.now()
    d = fd.strftime("%H:%M:%S %d-%m-%Y")
    return d
def paragraph():
    vvv = input()
    return vvv

def create_write():
    wr = open("BloknotSapis.csv", "a")
    print("Введите название заметки")
    wr.writelines("\t")
    wr.writelines(paragraph())
    wr.writelines("\n")
    print("Введите тело заметки")
    wr.writelines(wwod())
    #wr.write("\n")
    wr.writelines(" " + datenow())
    wr.writelines("\n")
    wr.close()
    identifikation()

def identifikation():
    w2 = open("BloknotSapis.csv", "r", encoding = "utf-8")
    array3 = []
    for line in w2:
        array3.append(line)
    w2.close()
    count4 = 1
    for i5 in array3:
        for j7 in i5:
            if(j7 == i5[0]):
                if(i5[1] == "\t"):
                    count4 = int(i5[0]) + 1
    for i in array3:
        for j in i:
            if(j == i[0]):
                print("Yes")
                if(j == "\t"):
                    inw = array3.index(i)
                    s5 = array3[inw]
                    s6 = s5.split()
                    print(s6)
                    c44 = str(count4)
                    s6.insert(0, c44 + "\t")
                    print(s6)
                    array3.pop(inw)
                    array3.insert(inw, " ".join(s6) + "\n")
                    count4 += 1
    print(array3)
    w3 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in array3:
        w3.writelines(i)
    w3.close()





#create_write()
def read():
    re = open("BloknotSapis.csv", "r")
    for line in re:
        print(line, end = "")
    re.close()
# read()
def find():
    print("Введите ID, заголовок или Дату, или Время котрое ищите")
    fin = input()
    fi = open("BloknotSapis.csv", "r")
    for line in fi:
        for i in line.split():
            if(i == fin):
                print(line)
    fi.close()
#find()
def zamena():
    print("Введите 7 чтобы удалить заголовок или 8 чтобы заменить слово")
    r = int(input())
    array = []
    if(r == 8):
        fi1 = open("BloknotSapis.csv", "r", encoding = "utf-8")
        print("Введите слово для которого произвести замену")
        finis = input()
        print("Введите слово для замены")
        finis1 = input()
        for line in fi1:
            array.append(line)
            for i in array:
                for j in i.split():
                    if(j == finis):
                        val = array.index(i)
                        safe = array[val]
                        array.remove(i)
                        ss = safe.split()
                        for i1 in ss:
                            if(i1 == finis):
                                val1 = ss.index(i1)
                                ss.remove(i1)
                                indexpod = len(ss) - 1
                                ss.pop(indexpod)
                                ss.pop(indexpod - 1)
                                ss.insert(indexpod - 1, datenow())
                                ss.insert(val1, finis1)
                                array.insert(val, " ".join(ss) + "\n")
        fi1.close()
        fi11 = open("BloknotSapis.csv", "w", encoding = "utf-8")
        for i in array:
            fi11.writelines(i)
        fi11.close()
    if(r == 7):
        print("Введите заголовок для которого произвести замену")
        finis4 = input()
        print("Введите новый заголовок для замены")
        finis5 = input()
        fi2 = open("BloknotSapis.csv", "r", encoding = "utf-8")
        for line in fi2:
            array.append(line)
        fi2.close()
        r1 = 0 #НАЧАЛО ИЗМ
        length1 = len(array)
        for i in array:
            if(finis4 in i):
                r1 = array.index(i)
                array.pop(r1)
                array.insert(r1, "\t" + finis5 + "\n")
                print(array)
        r2 = 0 #КОНЕЦ ИЗМ
        if(array[r1 + 1] != array[length1 - 1]):
            count = 1
            while("\t" not in array[r1 + count]):
                if("\t" in array[r1 + count + 1]):
                    r2 = r1 + count
                count += 1
            safe2 = array[r2]
            sss = safe2.split()
            indexpod1 = len(sss) - 1
            print(sss)
            sss.pop()
            print(sss)
            sss.pop()
            sss.insert(indexpod1, datenow())
            array.pop(r2)
            array.insert(r2, " ".join(sss) + "\n")
        else: 
            r2 = len(array) - 1
            safe3 = array[r2] 
            array.pop(r2)
            ssss = safe3.split()
            indexpod2 = len(ssss) - 1
            ssss.pop()
            ssss.pop()
            ssss.insert(indexpod2, datenow())
            array.insert(r2, " ".join(ssss) + "\n")
        print(array)
    fi3 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in array:
        fi3.writelines(i)
    fi3.close()
    identifikation()
def dele():
    list_array = []
    print("Введите слово из строки, которую хотите удалить")
    ww = input()
    fi111 = open("BloknotSapis.csv", "r", encoding = "utf-8")
    for line in fi111:
        list_array.append(line)
    for i11 in list_array:
        for j15 in i11.split():
            if(j15 == ww):
                iu = list_array.index(i11)
                list_array.pop(iu)
                list_array.insert(iu, datenow() + "\n")
    # for line in fi111:
    #     if(ww not in line):
    #         list_array.append(line)
    #     elif(ww in line):
    #         list_array.append(datenow() + "\n")
    fi111.close()
    fi1111 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in list_array:
        fi1111.writelines(i)
    fi1111.close()
def delallpar():
    list_array_del = []
    print("Введите заголовок заметки, которой хотите удалить")  ##"""УДАЛЯТЬ БУДЕМ ОТ ПОРАГРАФА ДО 4 Х ПРОБЕЛОВ ИЛИ ТАБА"""
    www = input()
    fi111 = open("BloknotSapis.csv", "r", encoding = "utf-8")
    for line in fi111:
        list_array_del.append(line)
    print(list_array_del)
    ind_nach = 0
    indexend = 0
    for i in list_array_del: ## ИЩЕМ НАЧАЛО, ИНДЕКС НУЖНОГО МЕСТА УДАЛЕНИЯ
        for j in i.split():
            if(j == www):
                print(j + "Yes")
                ind_nach = list_array_del.index(i)
    length = len(list_array_del)
    if(list_array_del[ind_nach + 1] != list_array_del[length - 1]):
        count = 1
        while("\t" not in list_array_del[ind_nach + count]):
            print(list_array_del[ind_nach + count])
            list_array_del.pop(ind_nach)
            list_array_del.pop(ind_nach)
            count = 0
    else: 
        indexend = len(list_array_del) - 1 
        count1 = 0
        while(list_array_del[indexend - count1] != list_array_del[ind_nach - 1]):
            list_array_del.pop() # ЕСЛИ ИНДЕКС НЕ УКАЗАН УДАЛЯЕТСЯ ПОСЛЕДНИЙ ЭЛЕМЕНТ
            count1 += 1
    #print(count)
    print(list_array_del)
    fi111.close()
    fi1111 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in list_array_del:
        fi1111.writelines(i)
    fi1111.close()

# def prov(argStr):
#     isOnlyDigits = True
#     count = 0
#     numarr = ["1","2","3","4","5","6","7","8","9","0"]
#     if(argStr == 10):
#         if(argStr[2] == "-" | argStr[5] == "-"):
#             for i in argStr:
#                 if(i in numarr & argStr[count] != 2 & argStr[count] != 5): 
#                     isOnlyDigits = True
#                 else: isOnlyDigits = False
#             count += 1
#         else: isOnlyDigits = False
#     return isOnlyDigits
                        


def exit(arg):
    while arg == 0: break

def main():
    print("1 Начать запись")
    print("2 Вывести заметки на экран")
    print("3 Поиск")
    print("4 Замена")
    print("5 Удаление частично")
    print("6 Удаление заметки")
    print("0 Выход")
    com = int(input())
    if(com == 1):
        create_write()
    if(com == 2):
        read()
    if(com == 3):
        find()
    if(com == 4):
        zamena()
    if(com == 5):
        dele()
    if(com == 6):
        delallpar()
    if(com == 0):
        exit(com)
def controlmain():
    print("Введите любое число для запуска кроме 0 и ноль если завершить")
    com1 = int(input())
    while(com1 != 0):
        main()
        return controlmain()
controlmain()