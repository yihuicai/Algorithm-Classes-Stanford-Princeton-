def IntegerMultiplication(x,y):
    ret = ""
    length = max(len(x),len(y))
    a = x[:-length/2]
    if a == "":
        a = "0"
    b = x[-length/2:]
    c = y[:-length/2]
    if c == "":
        c = "0"
    d = y[-length/2:]
    head = ""
    print a,b,c,d
    if len(a) > 4 or len(b) > 4:
        head = IntegerMultiplication(a,c)
    else:
        head = str(int(a)*int(c))
    tail = ""
    if len(b) > 4 or len(c) > 4:
        tail = IntegerMultiplication(b,d)
    else:
        tail = str(int(b)*int(d))
    mid = ""
    if len(a) > 4 and len(d) > 4:
        mid = AddNumbers(IntegerMultiplication(a,d),IntegerMultiplication(b,c))
    else:
        mid = str(int(a)*int(d) + int(b)*int(c))
    for i in range(length):
        head += "0"
    for j in range(length/2):
        mid += "0"
    ret = AddNumbers(head, mid)
    ret = AddNumbers(ret, tail)
    print "result"
    print ret
    return ret


def AddNumbers(m,n):

    m_len=len(m)
    n_len=len(n)
    i = m_len-1
    j = n_len-1
    flag = 0
    ret = ""
    while i!=-1 or j!=-1:
        if i == -1:
            numsum = str(int(n[j]) + flag)
            if len(numsum) > 1:
                flag = 1
                numsum = numsum[-1]
            else:
                flag = 0
            ret = numsum + ret
            j -= 1
        elif j == -1:
            numsum = str(int(m[i]) + flag)
            if len(numsum) > 1:
                flag = 1
                numsum = numsum[-1]
            else:
                flag = 0
            ret = numsum + ret
            i -= 1
        else:
            numsum = str(flag + int(m[i])+int(n[j]))
            if len(numsum) > 1:
                flag = 1
                numsum = numsum[-1]
            else:
                flag = 0
            ret = numsum + ret
            i -= 1
            j -= 1

    if flag == 1:
        ret="1"+ret

    return ret
#print AddNumbers("123","245")
print IntegerMultiplication("3141592653589793238462643383279502884197169399375105820974944592"
                             ,"2718281828459045235360287471352662497757247093699959574966967627")
