def check(x):
    stack = []
    for char in x:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return 'not balanced'
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return 'not balanced'
            if current_char == '{':
                if char != '}':
                    return 'not balanced'
            if current_char == '[':
                if char != ']':
                    return 'not balanced'
    if stack:
        return 'not balanced'
    return 'balanced'


x = '{([])'
print(check(x))
