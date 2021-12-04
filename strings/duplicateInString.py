from collections import defaultdict


def method1(arr):
    data = defaultdict(int)
    for i in range(len(arr)):
        data[arr[i]] += 1

    for i in data:
        if data[i] > 1:
            print(i, data[i])


def method2(arr):
    noOfChar = 256
    count = [0]*noOfChar
    for i in arr:
        count[ord(i)] += 1

    k = 0
    for i in count:
        if int(i) > 1:
            print(chr(k), str(i))
        k += 1


arr = ['a', 'a', 'b', 'b', 'c', 'd']
method1(arr)
method2(arr)
