def swap(a, st, end):
    a[st], a[end] = a[end], a[st]


def reverseList(a, st, end):
    while st <= end:
        swap(a, st, end)
        st += 1
        end -= 1


def recursiveReverse(a, st, end):
    if st >= end:
        return
    swap(a, st, end)
    recursiveReverse(a, st+1, end-1)


li = [1, 2, 3, 4, 5, 6]
n = len(li)
reverseList(li, 0, n-1)
# recursiveReverse(li, 0, n-1)
print(li)
