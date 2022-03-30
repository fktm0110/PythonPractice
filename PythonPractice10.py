import random


YN = "Y"
totalcount = 0 #정답이든 오답이든 실행될때마다 카운트+1
countcorrect = 0 #정답일때만 카운트 +1
correctpercent = 0 # (countcorrect / totalcount) * 100 => 정답률

while True :
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    correct = n1 * n2

    if YN == "Y" :
        result = int(input("{}*{}의 값은 ? ".format(n1,n2)))
        if correct == result:
            print("정답입니다.")
            countcorrect = countcorrect + 1
        else :
            print("오답입니다.")

        totalcount = totalcount + 1

        correctpercent = (countcorrect / totalcount) * 100

        YN = input("계속 하시겠습니까?(Y/N)")

    elif YN == "N":
        print("정답률은 {:0.0f}%입니다.".format(correctpercent))
        break