
#find combination for given string and for given length
while len(c) != pow(2, l):
    stri = ""
    for _ in range(l):
        stri += n[randint(0, 1)]
    if stri not in c:
        c.append(stri)
k = c.copy()