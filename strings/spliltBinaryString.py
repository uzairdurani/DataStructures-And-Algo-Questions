def SplitString(s, n):
    count0 = 0
    count1 = 0
    cnt = 0
    for i in range(n):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1
        if count0 == count1:
            cnt += 1

    if count0 != count1:
        return -1
    return cnt


str = '0111100010'
n = len(str)
print(SplitString(str, n))
