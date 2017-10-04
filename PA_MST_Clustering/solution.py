from Queue import PriorityQueue
from unionfind import unionfind
import sys

def Q1(f, k, length):
    pq = PriorityQueue(length)
    ret = {}
    count = 0
    first = f.readline()
    first = int(first)
    print first
    for j in range(1,first+1):
        ret[j] = [j]
    for i in range(124750):
        edge= f.readline()
        edge = edge.split(" ")
        a, b, c = int(edge[2][:-1]), int(edge[0]), int(edge[1])
        pq.put((a, b, c))
    max_spacing = 0
    while len(ret.keys())> k :
        to = -1
        from_i = -1
        #print len(ret.keys())
        # find maximum cost edge
        cost, node1, node2 = pq.get()
        # merge the clusters
        items = []
        for i in range(1,501):
            if ret.get(i) == None:
                continue
            if ret[i].count(node2) != 0:
                items = ret[i]
                from_i = i
            elif ret[i].count(node1) != 0:
                to = i
        if to == -1 or from_i == -1:
            continue
        ret[to] += items
        del ret[from_i]
        max_spacing = cost
    dic = {}
    c = 0
    for val in ret.values():
        for v in val:
            dic[v] = c
        c += 1
    a, b, c = pq.get() 
    while dic[b] == dic[c]:
        a, b, c = pq.get()
    
    print ret
    return a
        
def Q2(nodes, diff, nums_nodes, nums_bits):
    dic = {}
    node_cluster = {}
    u = unionfind(nums_nodes)
    count = 0
    # distance 0
    dic = {}
    count = nums_nodes
    for i in range(nums_nodes):
        a = nodes[i]
        if dic.get(nodes[i]) == None:
            dic[nodes[i]] = i
        else:
            if u.issame(i, dic[nodes[i]]) == False:
                u.unite(i, dic[nodes[i]])
                count -= 1
    # distance 1
    print count
    for i in range(nums_nodes):
        for j in range(nums_bits):
            #origin_j = nodes[i][j]
            n = list(nodes[i])
            if n[j] == "0":
                n[j] = "1"
            else:
                n[j] = "0"
            if dic.get("".join(n)) != None:
                if u.issame(i, dic["".join(n)]) == False:
                    count -= 1
                    u.unite(i, dic["".join(n)])
            #nodes[i][j] = origin_j
    # distance 2
    print count
    for i in range(nums_nodes):    
        for j in range(nums_bits-1):
            for k in range(j, nums_bits):
                #origin_j = nodes[i][j]
                #origin_k = nodes[i][k]
                n = list(nodes[i])
                if n[j] == "0":
                    n[j] = "1"
                else:
                    n[j] = "0"
                if n[k] == "0":
                    n[k] = "1"
                else:
                    n[k] = "0"
                
                if dic.get("".join(n)) != None:
                    if u.issame(i, dic["".join(n)]) == False:
                        u.unite(i, dic["".join(n)])
                        count -= 1
                #n[j] = origin_j
                #n[k] = origin_k

    return count

    
 
##################### Question 1 ##############################
num_lines = sum(1 for line in open('clustering.txt'))

f1 = open('clustering.txt', 'r')
print Q1(f1, 4, num_lines)


##################### Question 2 ##############################
f2 = open('clustering_big.txt', 'r')
no = f2.readline()
no = no.split(" ")
nextline = f2.readline()
nodes = []
while nextline:
    nodes.append("".join(nextline.split(" ")[:-1]))
    nextline = f2.readline()

print Q2(nodes, 3, int(no[0]), int(no[1][:-1]))
