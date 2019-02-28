'''
Pseudocode
BUBBLESORT(A)
for i=1 to A.length
    for j=A.length downto i+1
        if A[j]<A[j-1]
            exchange A[j] with A[j-1]
'''

#bubblesort
def bubblesort(A):
    for i in range(0,len(A)-1):
        for j in range(len(A)-1,i,-1):
            if(A[j]<A[j-1]):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp

#test
A = [31,41,59,26,41,58]
bubblesort(A)
print(A)
