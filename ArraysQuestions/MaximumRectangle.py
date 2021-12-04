def solve_hist(hist):
    hist.append(0)
    stack = [(-1, -1)]
    best_ans = 0
    for r_op, val in enumerate(hist):
        while stack[-1][0] > val:
            v, i = stack.pop()
            l_op = stack[-1][1]
            l_cl = l_op + 1
            ans = v * (r_op - l_cl)
            best_ans = max(ans, best_ans)
        stack.append((val, r_op))
        print(stack)
    return best_ans


def maxArea(M, n, m):
    for r in range(1, len(M)):
        for c in range(len(M[0])):
            if M[r][c] == 1:
                M[r][c] += M[r - 1][c]
    best_ans = 0
    for hist in M:
        ans = solve_hist(hist)
        best_ans = max(ans, best_ans)
    return best_ans


A = [[0, 1, 1, 0],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 0, 0]]

print(maxArea(A, 1, 2))
