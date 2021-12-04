def check(s1, s2):
    new = s1+s1
    if len(s1) == len(s2) and s2 in new:
        return True
    else:
        return False


s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
print(check(s1, s2))
