import sys

fileName = input("input fileName: ")
accesMode = "r"
count = 1

try :
    myFile = open(fileName, accesMode) #프로젝트 파일 내 abc.txt파일 존재 합니다. 입력 후 확인 부탁드립니다.
    line = myFile.readline()
    while line != "":
        print("{} : ".format(count) + line, end = '')
        line = myFile.readline()
        count = count+1
    myFile.close()
except FileNotFoundError :
    print("COULD NOT FOUND FILENAME")
except :
    error = sys.exc_info()[0]
    print("I am sorry something went wrong")
    print(error)
else :
    print("\n")
    print('No error, FileName is : {}'.format(fileName))