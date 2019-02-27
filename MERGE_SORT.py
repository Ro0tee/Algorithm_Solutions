'''
MERGE
Pseudocode

MERGE(A,p,q,r)
n = q-p+1
m = r-q
L = new integer[n+1]
R = new integer[m+1]
for j =1 to n
    L[j] = A[p+j-1]
for j=1 to m
    R[j] = A[q+j]
L[n+1] = inf
R[m+1]  inf
i = 1
j = 1
for k=p to r
    if L[i]<=R[j]
        A[k] = L[i]
        i = i+1
    else A[k] = R[j]
        j = j+1

==========================

MERGE-SORT
Pseudocode

MERGE-SORT(A,p,r)
if p<r
    q = (p+r)//2
    MERGE-SORT(A,p,q)
    MERGE-SORT(A,q+1,r)
    MERGE(A,p,q,r)

'''

#MERGE
def MERGE(A,p,q,r):
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
def MERGE_SORT(A,p,r):
    if(p<r):
        q = (p+r)//2
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q+1,r)
        MERGE(A,p,q,r)

#test
A = [31,41,59,26,41,58]
MERGE_SORT(A,0,len(A)-1)
print(A)
