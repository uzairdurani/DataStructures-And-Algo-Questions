def maxProfit(arr, n):
    profit = 0
    count = 0
    for i in range(1, n):

        if arr[i] > arr[i-1]:
            profit += (arr[i]-arr[i-1])
            count += 1

    return profit


arr = [7, 6, 4, 3, 1]
n = len(arr)
print(maxProfit(arr, n))
