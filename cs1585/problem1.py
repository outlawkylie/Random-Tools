import array as arr
import random
import time

t1 = 0
t2 = 0
t3 = 0
array1 = arr.array("i",[])

for x in range(1000):
    array1.append( random.randrange(0, 1) )
    t1 = time.process_time()
    
    #assuming multiply by itself means square each index value
    for y in range(len(array1)):
        array1[y] = array1[y]*array1[y]
    t2 = time.process_time()
    t3 = t3 + t2 - t1

print( t3 )
