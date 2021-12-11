def palindrome(s):

    count = []
    for word in s:
        letters = []
        psub = []
        for l in word:
            letters.append(l)
            if l not in psub:
                psub.append(l)

        for i in range(len(s)):
            for k in range(i+1, len(s)+1):
                sub = ('').join(s[i:k])
                #print (i,k,sub)
                if palindrome(sub) and sub not in psub:
                    psub.append(sub)

        count.append(len(psub))


dp = [[-1 for x in range(1000)]
      for y in range(1000)]
string = 'uziarkhan snga ye bikhe gaib ye waalaaah'
print(palindrome(string))
