def Triple(A, n, X):
    A.sort()
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            if A[i]+A[l]+A[r] == X:
                print(A[i], A[l], A[r])
                return True
            elif A[i]+A[l]+A[r] < X:
                l = +1
            else:
                r -= 1

    return False


def Find3Num(A, n, k):
    for i in range(n-1):
        s = set()
        curr_sum = k-A[i]
        for j in range(i+1, n):
            if curr_sum - A[j] in s:
                print("Triplet is", A[i], ", ", A[j], ", ", curr_sum-A[j])
                return True
            s.add(A[j])
    return False


A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
Find3Num(A, arr_size, sum)
