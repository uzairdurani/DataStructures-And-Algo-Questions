def factorial(N):
    # code here
    factorial = fact(N)
    lst = []
    while(factorial != 0):
        lst.append(factorial % 10)
        factorial = factorial//10
    return lst[::-1]


def fact(N):
    factorial = 1
    if N == 0:
        factorial = 1
    else:
        factorial = N*fact(N-1)
    return factorial


print(factorial(5))
