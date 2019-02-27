'''
Pseudocode

REINSERTION(A,n)
if(n>=1)
    REINSERTION(A,n-1)
    key = A[n]
    i = n-1
    while i>0 and A[i]>key
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key

'''

def reinsertion_sort(A,n):
    if(n>=1):
        reinsertion_sort(A,n-1)
        key = A[n]
        i = n-1
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i -=1
        A[i+1] = key


#test
A = [5,4,3,2,1,0]
reinsertion_sort(A,len(A)-1)
print(A)