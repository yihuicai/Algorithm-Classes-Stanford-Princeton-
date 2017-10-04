from Queue import PriorityQueue
import sys

def Q1(f):
    njobs = f.readline()
    njobs = int(njobs)
    jobWeight=[]
    jobLength=[]
    total=[]
    pq = PriorityQueue(njobs)
    length = 0

    for i in range(njobs):
        l = f.readline()
        l=l.split(" ")
        jobWeight.append(int(l[0]))
        jobLength.append(int(l[1]))
        score = (jobLength[-1] - jobWeight[-1], -jobWeight[-1])
        #score = float(jobLength[-1])/float(jobWeight[-1])
        pq.put((score, i))

    for i in range(njobs):
        score, index = pq.get()
        length += jobLength[index]
        total.append(length*jobWeight[index])

    return sum(total)

def Q2(f):
    n = f.readline()
    n = n.split(" ")
    nvertices = int(n[0])
    nedges = int(n[1])
    print nedges
    E = {} # edges key: node0 ,value: list[(cost, node1)]
    V = [] # original Vertices
    V2 = {} # collected
    #l[0], l[1] one node, l[2] edge between
    for i in range(nedges):
        lo = f.readline()
        lo = lo.split(" ")
        lo[2] = lo[2][:-1]
        l = []
        for li in lo:
            l.append(int(li))
            
        if E.get(l[0]) == None:
            E[l[0]] = [(l[2], l[1])]
            V.append(l[0])
        else:
            E[l[0]].append((l[2], l[1]))
            
        if E.get(l[1]) == None:
            E[l[1]] = [(l[2], l[0])]
            V.append(l[1])
        else:
            E[l[1]].append((l[2], l[0]))
    minret = sys.maxint
    for j in range(len(V)):
        VX = []
        for vx in V:
            VX.append(vx)
        V2 = {}
        v0 = VX[j]
        V2[v0] = [(0,-1)]
        VX.remove(v0)
        pq = PriorityQueue(2*nedges)
        for i in E[v0]:
            pq.put(i)
        ret = 0

        while len(VX) > 0:
            cost, v1 = pq.get()
            while True:
                if V2.get(v1) == None:
                    break
                cost, v1 = pq.get()
            V2[v1] = [(cost, v1)]
            #V2[v0].append(cost)
            VX.remove(v1)
            for i in E[v1]:
                pq.put(i)
            ret += int(cost)
        print ret
        minret = min(minret, ret)
        
    return minret
    

f1 = open('jobs.txt', 'r')
print Q1(f1)

#f2 = open('edges.txt', 'r')

# sum 69120882574
# sum 67311454237
#print Q2(f2)
