dp = dict()


def wordBreak(line, dictionary):
    global dp
    # Complete this function
    length = len(line)
    # print(length)
    if length == 0:
        return 1
    if line in dp:
        return 1
    for i in range(1, length+1):
        word = line[:i]
        boolean = 0
        for j in dictionary:
            if j == word:
                dp[word] = 1
                boolean = 1
                break
        if boolean == 1 and wordBreak(line[i:], dictionary):
            return 1
    return 0


B = {"i", "like", "sam",
     "sung", "samsung", "mobile",
     "ice", "cream", "icecream",
     "man", "go", "mango"}
A = "ilike"
print(wordBreak(A, B))
print(dp)
