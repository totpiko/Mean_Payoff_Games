import time

#================= DEFINE FUNCTIONS ====================
def findmax(node, step):
    values = []
    for key in w:
        if key.startswith(node) is False:
            continue
            #remove the part by which it starts
        if step!=0:
            values.append(w[key] + vector_past[key[len(node):]])
        else:
            values.append(w[key])
    if(len(values)==0):
        values.append(0)
    return max(values)

def findmin(node, step):
    values = []
    for key in w:
        if key.startswith(node) is False:
            continue
            #remove the part by which it starts
        if step!=0:
            values.append(w[key] + vector_past[key[len(node):]])
        else:
            values.append(w[key])
    if(len(values)==0):
        values.append(0)
    return min(values)




#================= DEFINE GRAPH ====================

vertices = ['gio', 'sos', 'txz', 'fty', 'nrv', 'qaq', 'nsm', 'axe', 'kvj', 'cqa',
            #'avp', 'zrp', 'zwo', 'kcg', 'zpe', 'twc', 'zro', 'htw', 'nkd', 'awk',
            #'dqb', 'pub', 'zue', 'wap', 'tsf', 'fce', 'pfn', 'prc', 'pzw', 'idy',
            #'fwr', 'jot', 'rsh', 'hbq', 'jlk', 'pny', 'qwe', 'ulz', 'ell', 'cex',
            #'bhh', 'gih', 'yij', 'vaa', 'xnn', 'fts', 'xxl', 'cgh', 'gcz', 'yfr',
            'vuo', 'ctb', 'cbp', 'tto', 'gat', 'cpa', 'pnj', 'ohd', 'sbm', 'unk']
            #'xue', 'ukp', 'kod', 'mej', 'jve', 'oqp', 'pxg', 'gxz', 'tlm', 'bsa',
            #'zrm', 'foj', 'xhq', 'lcy', 'dze', 'evs', 'dwm', 'ioy', 'vrj', 'zkd',
            #'nfv', 'yop', 'mbl', 'dwf', 'ccv', 'swc', 'yza', 'dbt', 'akx', 'mxo',
            #'gol', 'rum', 'zti', 'nxy', 'gnu', 'xqh', 'mqy', 'cvc', 'agy', 'geo']
player1 = [ 'gio', 'sos', 'txz', 'fty', 'nrv', 'qaq', 'nsm', 'axe', 'kvj', 'cqa']
            #'avp', 'zrp', 'zwo', 'kcg', 'zpe', 'twc', 'zro', 'htw', 'nkd', 'awk',
            #'dqb', 'pub', 'zue', 'wap', 'tsf', 'fce', 'pfn', 'prc', 'pzw', 'idy',
            #'fwr', 'jot', 'rsh', 'hbq', 'jlk', 'pny', 'qwe', 'ulz', 'ell', 'cex',
            #'bhh', 'gih', 'yij', 'vaa', 'xnn', 'fts', 'xxl', 'cgh', 'gcz', 'yfr']
player2 = [ 'vuo', 'ctb', 'cbp', 'tto', 'gat', 'cpa', 'pnj', 'ohd', 'sbm', 'unk']
            #'xue', 'ukp', 'kod', 'mej', 'jve', 'oqp', 'pxg', 'gxz', 'tlm', 'bsa',
            #'zrm', 'foj', 'xhq', 'lcy', 'dze', 'evs', 'dwm', 'ioy', 'vrj', 'zkd',
            #'nfv', 'yop', 'mbl', 'dwf', 'ccv', 'swc', 'yza', 'dbt', 'akx', 'mxo',
            #'gol', 'rum', 'zti', 'nxy', 'gnu', 'xqh', 'mqy', 'cvc', 'agy', 'geo']
w = {'giovuo': -1}#, 'giozrm': 1, 'gioccv': 1, 'vuosos': 1, 'pfnctb': -1, 'cvcgio': 1, 'pnjxxl': -1}

#successors = {'y':'xz','x':'y','v':'yz','z':'w','w':'z'}

#================= START ALGORITHM ====================
k = 0  #counter for the steps
n = len(vertices)  #number of vertices
W = max(abs(i) for i in w.values())  #value of the highest weight in absolute value
vector_current = {}
vector_past = {}
#f = open('workfile', 'w')

#test

while k != 4*n**3*W:
    #start1 = time.time()

    for a in vertices:
        if a in player1:
            value = findmax(a, k)
            #value2 = findmax2(a,k)
            vector_current[a] = value

        else:
            value = findmin(a, k)
            vector_current[a] = value
    k += 1

    #check if current vector and the past one are not the 'same'

    vector_past_norm = []
    vector_current_norm = []
    for a in vector_past.values(): vector_past_norm.append(a/k-1)
    for a in vector_current.values(): vector_current_norm.append(a/k)

    #if the vectors are the same end the calculation
    if(vector_current_norm == vector_past_norm):
        break
    vector_past = dict(vector_current)
    #end1 = time.time()
    #f.write(str(end1-start1)+"\n")




#The total sums of the value
#print (vector_current)
lower_bound ={}
upper_bound ={}
#Normalized value for the node
for key,value in vector_current.items():
    v_norm = value/k
    vector_current[key] = v_norm
    lower_bound[key] = v_norm - 1/(2*n*(n-1))
    upper_bound[key] = v_norm + 1/(2*n*(n-1))
print (lower_bound)
print (vector_current)
print (upper_bound)


#TODO
#12) how does iteration time increase per iteration
#13) create a GIT folder
#12) measure the time it actually takes to calculate, amount of CPU time consumed per process
# 6) generate the graphs - random weighted graph generator, W should be a parameter
# 5) test scripts

# 4) benchmarking
# 7) paper for examples for mean payoff games
# 8) check the one with two loops - in one of the papers
# 9) multiBDDs and BDDs - what operations can they perform with the libraries(min, max)
#10) ROBDD ordered BDD
#11) find libraries for BDD and MTBDD
#14) write introduction a general intro for BDD/MTBDD and the MPG

#TODO2
# 1) end condition - look at the ordering, why does it not match
# 2) rounding up - how exactly tackle that


#OLD CODE
#def findmax(node, step):
#    values = []
#    for b in successors[node]:
#        if step != 0:
#            values.append(w[node + b] + vector_past[b])
#        else:
#            values.append(w[node + b])
#    return max(values)

#def findmin(node, step):
#    values = []
#    for b in successors[node]:
#         if step != 0:
#            values.append(w[node + b] + vector_past[b])
#         else:
#            values.append(w[node + b])
#    return min(values)