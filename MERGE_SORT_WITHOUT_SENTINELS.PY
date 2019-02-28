'''
MERGE_WITHOUT_SENTINELS
Pseudocode

MERGE(A,p,q,r)
n = q-p+1
m = r-q
L = new integer[n]
R = new integer[m]
for j =1 to n
    L[j] = A[p+j-1]
for j=1 to m
    R[j] = A[q+j]
i = 1
j = 1
for k=p to r
    if i>n and j<=m:
        A[k] = R[j]
        j = j+1
    if i<=n and j>m:
        A[k] = L[i]
        i = i+1
    if i<=n and j<=m
        if L[i]<=R[j]
            A[k] = L[i]
            i = i+1
        else A[k] = R[j]
            j = j+1

==========================

MERGE-SORT-WITHOUT-SENTINELS
Pseudocode

MERGE-SORT-WITHOUT-SENTINELS(A,p,r)
if p<r
    q = (p+r)//2
    MERGE-SORT(A,p,q)
    MERGE-SORT(A,q+1,r)
    MERGE(A,p,q,r)

'''

#MERGE
def merge(A,p,q,r):
    n = q-p+1
    m = r-q
    L = [0 for i in range(0,n)]
    R = [0 for i in range(0,m)]
    for j in range(0,n):
        L[j] = A[p+j]
    for j in range(0,m):
        R[j] = A[q+j+1]
    i = 0
    j = 0
    for k in range(p,r+1):
        if(i>n-1 and j<=m-1):
            A[k] = R[j]
            j = j+1
        if(i<=n-1 and j>m-1):
            A[k] = L[i]
            i = i+1
        if(i<=n-1 and j<=m-1):
            if(L[i]<=R[j]):
                A[k] = L[i]
                i = i+1
            else:
                A[k] = R[j]
                j = j+1

#MERGE-SORT
def merge_sort(A,p,r):
    if(p<r):
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

#test
A = [31,41,59,26,41,58]
merge_sort(A,0,len(A)-1)
print(A)
