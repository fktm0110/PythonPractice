def listProd(a,b,n):
    a=[]
    b=[]
    sum=0

    for steps in range(n):
        temp = int(input("a[{}]리스트의 요소 입력".format(steps)))
        a.append(temp)
    for steps in range(n):
        temp = int(input("b[{}]리스트의 요소 입력".format(steps)))
        b.append(temp)

    for steps in range(n):
       sum = sum + (a[steps]*b[steps])

    return sum

n = int(input("배열의 크기를 입력하세요 : "))
a = []
b = []

print("크기가 {}인 두 리스트의 각 원소들을 곱하여 더한 값은 {} 입니다.".format(n,listProd(a,b,n)))



