file_path = "./IntegerArray.txt"
with open(file_path,"r") as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i]=int(lines[i])
def merge_sort(array):
    global temp
    if len(array)>1:
        m = len(array)//2
        lefthalf = array[:m]
        righthalf = array[m:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[k] = lefthalf[i]
                k = k+1
                i = i+1
            else:
                temp = temp + len(lefthalf)-i
                array[k] = righthalf[j]
                k = k+1
                j = j+1
        while i<len(lefthalf):
            array[k]=lefthalf[i]
            k=k+1
            i=i+1
        while j<len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1

temp =0 
merge_sort(lines)

print(temp)
