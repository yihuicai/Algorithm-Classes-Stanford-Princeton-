import sys
from Queue import PriorityQueue

def Q1(f):
    nsym = f.readline()
    nsym = int(nsym)
    sym = PriorityQueue(nsym+1)
    i = 0
    maxweight=0
    while i < nsym:
        newline = f.readline()
        sym.put((int(newline), 0))
        i += 1
        maxweight = max(int(newline), maxweight)
    k = 0
    max_len = 0
    while k < nsym - 1:
        weight1, n1 = sym.get()
        weight2, n2 = sym.get()
        
        lens = max(n1,n2)+1
        max_len = max(lens, max_len)
        sym.put((weight1 + weight2, lens))
        k += 1
        
    return max_len


def Q2(f):
    nsym = f.readline()
    nsym = int(nsym)
    sym = PriorityQueue(nsym+1)
    i = 0
    maxweight=0
    while i < nsym:
        newline = f.readline()
        sym.put((int(newline), 0))
        i += 1
        maxweight = max(int(newline), maxweight)
    k = 0
    max_len = 0
    min_len = 0
    while k < nsym - 1:
        weight1, n1 = sym.get()
        weight2, n2 = sym.get()   
        if weight1 == maxweight or weight2 == maxweight:
            min_len = max_len
        
        lens = max(n1,n2)+1
        max_len = max(lens, max_len)
        sym.put((weight1 + weight2, lens))
        k += 1
        
    return max_len - min_len

def Q3(f):
    nvertices = f.readline()
    nvertices = int(nvertices)
    i = 0
    dic = {}
    V = [-1]
    while i < nvertices:
        line = f.readline()
        V.append(int(line))
        i += 1
    weight = 0
    dic[0] = 0
    dic[1] = V[1]
    dics = {}
    dics[0] = []
    dics[1] = [1]
    
    for i in range(2,nvertices+1):
        if dic[i-1] > dic[i-2] + V[i]:
            dic[i] = dic[i-1]
            val = []
            val = dics[i-1]
            dics[i] = []
            dics[i] += val
        elif dic[i-1] < dic[i-2] + V[i]:
            dic[i] = dic[i-2] + V[i]
            val = []
            val = dics[i-2]
            dics[i] = []
            dics[i] += val
            dics[i].append(i)
    print dics[nvertices]
    find = [1, 2, 3, 4, 17, 117, 517, 997]
    a = dics[nvertices]
    res = {}
    for i in a:
        res[i] = 0
    ret = ""
    for r in find:
        if res.get(r) != None:
            ret += "1"
        else:
            ret += "0"

    return ret

"""
f1 = open('huffman.txt', 'r')
print Q1(f1)
"""
f2 = open('mwis.txt', 'r')
print Q3(f2)
