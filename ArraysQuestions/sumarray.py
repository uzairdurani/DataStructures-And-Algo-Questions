
def twoSum(nums, target: int):
    i, j = 0, 0
    n = len(nums)
    value = 0
    while j < n and value < target:
        if value == target:
            print(i, j)
            break
        value += nums[j]
        j += 1

    if value == target:
        print(i, j-1)

    if value > target:

        while i < n:
            if value == target:
                print(i, j-1)
                break
            value -= nums[i]
            i += 1

    elif value < target:

        while j < n:

            if value == target:
                print(i, j-1)
                break
            value += nums[j]
            j += 1


twoSum([3], 6)
