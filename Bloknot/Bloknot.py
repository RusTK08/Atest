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
    count = 0
    st = str(count)
    wr = open("BloknotSapis.csv", "a")
    print("Введите название заметки")
    wr.writelines("    ")
    wr.writelines(paragraph())
    wr.writelines("\n")
    print("Введите тело заметки")
    wr.writelines(wwod())
    #wr.write("\n")
    wr.writelines(" " + datenow())
    wr.writelines("\n")
    wr.close()
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
    array = []
    print("Введите слово для которого произвести замену")
    finis = input()
    count = 0
    print("Введите слово для замены")
    finis1 = input()
    fi1 = open("BloknotSapis.csv", "r", encoding = "utf-8")
    for line in fi1:
        for i in line:
            array.append(i)
    for i in array:
        if(i == finis):
            val = array.index(i)
            array.remove(i)
            array.insert(val, finis1 + " ")
    fi1.close()
    fi11 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in array:
        fi11.writelines(i)
    fi11.close()
def dele():
    list_array = []
    print("Введите слово из строки, которую хотите удалить")
    ww = input()
    fi111 = open("BloknotSapis.csv", "r", encoding = "utf-8")
    for line in fi111:
        if(ww not in line):
            list_array.append(line)
    fi111.close()
    fi1111 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in array:
        fi1111.writelines(i + "\n")
    fi1111.close()
def delallpar():
    list_array_del = []
    print("Введите заголовок заметки, которой хотите удалить")  ##"""УДАЛЯТЬ БУДЕМ ОТ ПОРАГРАФА ДО 4 Х ПРОБЕЛОВ ИЛИ ТАБА"""
    www = input()
    fi111 = open("BloknotSapis.csv", "r", encoding = "utf-8")
    for line in fi111:
        list_array_del.append(line)
    fi111.close()
    fi1111 = open("BloknotSapis.csv", "w", encoding = "utf-8")
    for i in array:
        for j in i:
            if(j == www):
                ind_nach = list_array_del.index(i)
                count = 0
                while(j != "    "):
                    list_array_del.pop(ind_nach + count)
                    count += 1
    for i in list_array_del:
        fi1111.writelines(i + "\n")
    fi1111.close()
def exit(arg):
    while arg == 0: break
# def priem():
#     num = int(input())
#     return num
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