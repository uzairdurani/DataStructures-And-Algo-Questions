def PairSum(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) == k:
                count += 1
    print(count)


def getPairsCount(arr, n, sum):

    m = [0] * (int(1e6)+1)

    for i in range(0, n):
        m[arr[i]] += 1

    twice_count = 0

    for i in range(0, n):

        twice_count += m[sum - arr[i]]

        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    return int(twice_count / 2)


def getPairCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]

        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    print(unordered_map)

    return count


arr = [1, 5, 2, 1]
# PairSum(arr, 50)
n = len(arr)
# print(getPairsCount(arr, n, 50))
print(getPairCount(arr, n, 6))
