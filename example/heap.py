# time complexity: O(nlogn)
# space complexity: O(n)

def makeHeap(arr,end):
    i=(end-1)/2
    while i>=0:
        left=i*2+1
        right=i*2+2
        max=left
        if right <= end and arr[right]>arr[left]:
            max=right
        if arr[max]>arr[i]:
            arr[i]=arr[i]^arr[max]
            arr[max]=arr[i]^arr[max]
            arr[i]=arr[i]^arr[max]
        i-=1

def heapSort(arr):
    i = len(arr)-1
    while i:
        makeHeap(arr, i)
        print (arr)
        if arr[0]!= arr[i]:
            arr[0]=arr[0]^arr[i]
            arr[i]=arr[0]^arr[i]
            arr[0]=arr[0]^arr[i]
        i-=1
    return arr

arr = [1, -100, 38, 79, 21, 14, 2000]
heapSort(arr)
print (arr)
