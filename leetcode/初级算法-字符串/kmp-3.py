# encoding = utf-8
def pnext(pstr):
    i = 0
    j = 1
    m = len(pstr)
    plist = [0] * m
    while j < m:
        if pstr[i] == pstr[j]:
            plist[j] = i + 1
            i += 1
            j += 1
        elif i == 0:
            plist[j] = 0
            j += 1
        else:
            i = plist[i - 1]
    return plist
def kmp(allstr,substr):
    m = len(allstr)
    n = len(substr)
    plist = pnext(substr)
    print(plist)
    i,j = 0,0
    while i < m and j < n:
        if substr[j] == allstr[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = plist[j-1]
    if j == n:
        return i - j
    else:
        return -1

string = 'abcxabcdaacdabcy'
substring = 'aacdabcy'
plist = pnext(substring)
index = kmp(string,substring)
# pnext2 = gen_pnext2(substring)
# out = KMP_algorithm(string, substring)
print(plist)
print(index)


