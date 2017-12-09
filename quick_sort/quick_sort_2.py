def quicksort(array):
    qsort(array,0,len(array)-1)
def qsort(array,low,high):
    if low<high:
        pivot = partition(array,low,high)
        qsort(array,low,pivot-1)
        qsort(array,pivot+1,high)
def partition(array,low,high):
    pivot = array[low]
    i = low+1
    for j in range(i,high+1):
        if array[j]<pivot:
            swap(array,j,i)
            i = i + 1
    swap(array,low,i-1)
            
    print(array)    
    return i-1
def swap(array,low,high):
    temp = array[low]
    array[low] = array[high]
    array[high] = temp

alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print(alist)
