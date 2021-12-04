def Max_Min_heights(arr, k):
    arr.sort()
    ans = arr[-1] - arr[0]
    for i in range(len(arr)-1):
        maxi = max(arr[i]+k, arr[-1]-k)
        mini = min(arr[i+1]-k, arr[0]+k)
        if mini < 0:
            continue
        ans = min(ans, maxi-mini)
    return ans


arr = [1, 4, 6]
print(Max_Min_heights(arr, k=3))
