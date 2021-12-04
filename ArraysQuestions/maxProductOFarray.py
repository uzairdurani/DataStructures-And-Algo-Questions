def maxProduct(arr):
    minVal = arr[0]
    maxVal = arr[0]
    maxProduct = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            maxVal, minVal = minVal, maxVal
        maxVal = max(arr[i], maxVal*arr[i])
        minVal = min(arr[i], minVal*arr[i])

        maxProduct = max(maxProduct, maxVal)
    return maxProduct
