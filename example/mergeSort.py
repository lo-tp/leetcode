# worst: O(nlogn)
# ave: O(nlogn)

def mg(arr):
    if len(arr)>1:
        m=len(arr)/2
        l=arr[:m]
        r=arr[m:]
        lIndex=0
        rIndex=0
        rSize=len(r)
        lSize=len(l)
        mg(l)
        mg(r)
        i=0
        while lIndex< lSize and rIndex < rSize:
            if l[lIndex]<r[rIndex]:
                arr[i]=l[lIndex]
                lIndex+=1
            else:
                arr[i]=r[rIndex]
                rIndex+=1
            i+=1
        while lIndex<lSize:
            arr[i]=l[lIndex]
            lIndex+=1
            i+=1
        while rIndex<rSize:
            arr[i]=r[rIndex]
            rIndex+=1
            i+=1

arr = [1, -100, 38, 79,-100, 21,3879, 14, 2000]
mg(arr)
print (arr)
