import random

def sort(arr):
    length = len(arr)
    for j in range(1, length):
        key = arr[j]
        i = j-1
        while i >= 0:
            if(arr[i]>key):
                print arr
                arr[i+1] = arr[i]
            else:
                break
            i = i-1
        print arr
        arr[i+1] = key
            
    print arr


unsorted =  [random.randint(0,50) for r in xrange(30)] 

print unsorted
sort(unsorted)
