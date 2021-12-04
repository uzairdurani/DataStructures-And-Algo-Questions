def merge(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged


arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(arr))
