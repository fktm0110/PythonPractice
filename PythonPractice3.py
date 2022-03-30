def factorial(n):
    result = 1
    for steps in range(1, n+1):
        result = result*steps
    return result

n=int(input("input number : "))

print("{}!의 값은 {}입니다.".format(n, factorial(n)))


