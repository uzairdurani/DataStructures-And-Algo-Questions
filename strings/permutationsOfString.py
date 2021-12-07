def permute(arr, idx):
    if len(arr) == 1:
        print((arr))
        return
    for i in range(len(arr)):
        arr[i], arr[idx] = arr[idx], arr[i]
        permute(arr, idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]


def permute2(S):
    def build_list(S, L, s, n):
        if len(s) == n:
            L.append(s)
            return

        for c in S:
            build_list(S.replace(c, ""), L, s+c, n)

    L = []
    s = ""
    A = sorted(S)
    build_list("".join(A), L, s, len(S))
    return L


arr = 'abc'
# permute(arr, 0)
print(permute2(arr))
