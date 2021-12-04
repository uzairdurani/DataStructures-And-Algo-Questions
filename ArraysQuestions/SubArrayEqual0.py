def SumArray(arr, n):
    n_sum = 0
    s = set()
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(arr[i])]

    return False
