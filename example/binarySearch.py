# time O(logn)
# space O(1)

def bs(arr, target):
    s=0
    e=len(arr)-1
    while s<=e:
        m=s+(e-s)/2
        if arr[m]>target:
            e=m-1
        elif arr[m]<target:
            s=m+1
        else:
            return m
    return -1
