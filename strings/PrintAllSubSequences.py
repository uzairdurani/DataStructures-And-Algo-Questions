def Subsequences(Str, target):
    if len(Str) == 0:
        print(target, end=' ')
        return

    Subsequences(Str[1:], target+Str[0])
    Subsequences(Str[1:], target)


Subsequences('123', '')
