'''
Problem:
    Describe a Θ(nlgn)-time algorithm that, given a set S of n integers and another integer x, determines whether or not there exists two elements of S whose sum is exactly x.

Pseudocode

PAIR_EXIST(S,x)
MERGE-SORT(S,1,S.length)
for j=1 to S.length
    if(BINARY_SEARCH(S,x-S[j])!= NIL)
        return true
return false

'''

#MERGE
def merge(A,p,q,r):
    n = q-p+1
    m = r-q
    L = [0 for i in range(0,n+1)]
    R = [0 for i in range(0,m+1)]
    for j in range(0,n):
        L[j] = A[p+j]
    for j in range(0,m):
        R[j] = A[q+j+1]
    L[n] = float("inf")
    R[m] = float("inf")
    i = 0
    j = 0
    for k in range(p,r+1):
        if(L[i]<=R[j]):
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

#MERGE-SORT
def merge_sort(A,p,r):
    if(p<r):
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

#BINARY_SEARCH
def binary_search(A,v,low,high):
    mid = (low+high)//2
    if(mid >=0 and mid < high):
        if(A[mid] == v):
            return mid
        elif(A[mid] > v):
            low = mid+1
        else:
            high = mid-1
        binary_search(A,v,low,high)
    return None

#PAIR_EXIST
def pair_exist(S,x):
    merge_sort(S,0,len(S)-1)
    for j in range(0,len(S)-1):
        if(binary_search(S,x-S[j],0,len(S)-1)!=None):
            return True
    return False

#test
S = [0,1,2,5,7,9]
x = 9
print(pair_exist(S,x))
x = 13
print(pair_exist(S,x))

