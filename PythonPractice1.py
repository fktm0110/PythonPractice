number = input("input number : ")
number = int(number)
sum = 0

for steps in range(1,number+1) :
    sum = sum+steps
print("1부터 {}까지의 합은 {}입니다.".format(number,sum))