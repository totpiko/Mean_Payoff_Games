import time
#import thesis_1

times=[]
for x in range(0,1):
    start = time.time()
    exec(open('thesis_1.py').read())
    #exec('thesis_1')
    #print(thesis_1.player2)
    end = time.time()
    times.append(end-start)

avg = sum(times)/len(times)
print ("Total time: %4.3f seconds" %(avg))
