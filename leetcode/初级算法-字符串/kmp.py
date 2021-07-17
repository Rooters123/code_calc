# encoding = utf-8

def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    index, m = 0, len(substring)
    pnext = [0]*m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index!=0):
            index = pnext[index-1]
        else:
            pnext[i] = 0
            i += 1
    return pnext

def gen_pnext2(substr):
    i = 0
    j = 1
    m = len(substr)
    while j < m:
        if substr[i] == substr[j]:
            pnext[j] = i + 1
            i += 1
            j += 1
        elif i==0:
            pnext[j] = 0
            j += 0
        else:
            i = pnext[i-1]

def kmp(strs,substr):
    m = len(strs)
    n = len(substr)
    pnext = gen_pnext2(substr)
    print(pnext)
    i , j= 0 , 0
    while i < m and j < n:
        if strs[i] == substr[j]:
            i = i + 1
            j = j + 1
        elif j != 0:
            j = pnext[j - 1]
        else:
            # 如果找到头之后，j相当于从头开始没有匹配i的，所以需要移动总的指针
            i = i + 1
    if j == n:
        return i - j
    else:
        return -1



if __name__ == "__main__":
    string = 'BBC ABCDAB ABCDABCDABDE'
    # substring = 'ABCDABD'
    substring = 'aaabadc'
    pnext = kmp(string,substring)
    # pnext2 = gen_pnext2(substring)
    # out = KMP_algorithm(string, substring)
    print(pnext)
    # print(pnext2)