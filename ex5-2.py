def isOdd(num):
    num=int(num)
    if num % 2 == 0:
        return False
    else:
        return True
n = eval(input())
print(isOdd(n))
