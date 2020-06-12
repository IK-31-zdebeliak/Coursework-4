from datetime import datetime
import time
import sys
counter_compare = 0
counter_replace = 0

server_file = sys.argv[1]

handle = open(server_file, "r")
shell_array = handle.read()
handle.close()
print(shell_array)
shell_array = shell_array.split()
print(shell_array)
for i in range(0, len(shell_array)):
    shell_array[i] = int(shell_array[i])
print(type(shell_array))
print(shell_array)
print("Array before shell", shell_array )

start_time = datetime.now()
s = ''' '''
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = shell_array
shellSort(alist)
print('Array after shaker', shell_array )
print(" Lenght:", len(shell_array))
print("Time:")
print(datetime.now() - start_time)
for i in range(0, len(shell_array)):
    shell_array[i] = str(shell_array[i])
result =''.join(shell_array)
handle = open("server_outcoming.txt", "w")
handle.write(result)
handle.close()
