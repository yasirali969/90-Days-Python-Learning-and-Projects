import time

# Give time in second since 1970
print(time.time())

# give time in human readable form
print(time.ctime())

# take -seconds to pause to print output
print(time.sleep(5))

# print local time
print(time.localtime())


#print local time in proper format 
t=time.localtime()
print("%Y-%M-%D %H:%M:%S",time.localtime())

# High-precision timer for measuring performance or time intervals
# it tell how much time program or (loops(while,for)) take to run program
print(time.perf_counter())