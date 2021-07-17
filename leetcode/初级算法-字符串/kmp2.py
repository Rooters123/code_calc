# encoding = utf-8
def get_pnext(substr):
    i = 0
    j = 1
    m = len(substr)
    pnext = [0] * m
    while j < m:
        if substr[i] == substr[j]:
            pnext[j] = i + 1
            i = i + 1
            j = j + 1
        elif i == 0:
            pnext[j] = 0
            j = j + 1
        else:
            i = pnext[i - 1]
    return pnext
def kmp(substr,allstr):
    m = len(allstr)
    n = len(substr)
    pnext = get_pnext(substr)
    print(pnext)
    i,j = 0,0
    while i < m and j < n:
        if substr[j] == allstr[i]:
            i += 1
            j += 1
        elif j!=0:
            j = pnext[j - 1]
        else:
            i = i + 1
    if j == n:
        return i - j
    else:
        return -1
if __name__ == "__main__":
    string = 'abcxabcdaacdabcy'
    substring = 'aacdabcy'
    pnext = kmp(substring,string)
    # pnext2 = gen_pnext2(substring)
    # out = KMP_algorithm(string, substring)
    print(pnext)