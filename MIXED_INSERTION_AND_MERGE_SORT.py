'''
Pseuocode
MIXED_SORT(A,p,r,k)
if p<r
    if r-p<k
        INSERTION_SORT(A,p,r)
    else q=(p+r)//2
    MIXED_SORT(A,p,q,k)
    MIXED_SORT(A,q+1,r,k)
    MERGE(A,p,q,r)

'''

def insertion_sort(A,p,r):
    for j in range(p+1,r+1):
        key = A[j]
        i = j-1
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i -=1
        A[i+1] = key

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

def mixed_sort(A,p,r,k):
    if(p<r):
        if(r-p<k):
            insertion_sort(A,p,r)
        else:
            q = (p+r)//2
            mixed_sort(A,p,q,k)
            mixed_sort(A,q+1,r,k)
            merge(A,p,q,r)

#test
A = [31,41,59,26,41,58]
mixed_sort(A,0,len(A)-1,2)
print(A)