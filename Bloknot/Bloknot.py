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
    wr.writelines()
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
    re.close
# read()
def find():
    print("Введите ID Заголовок или Дату Или Время")
    fin = input()
    fi = open("BloknotSapis.csv", "r")
    for line in fi:
        for i in line.split():
            if(i == fin):
                print(line)
    fi.close
find()