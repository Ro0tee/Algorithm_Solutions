'''
Problem:
Rewrite the Insertion-Sort procedure to sort into nonincreasing instead of nondecreasing order

Pseudocode

SOLUTION(A)
for j = 2 to length[A]
    key = A[j]
    i = j-1
    while i>0 and A[i]<key
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key

'''

def insertion_sort_nonincreasing(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while(i>=0 and A[i]<key):
            A[i+1] = A[i]
            i -=1
        A[i+1] = key


#test
A = [31,41,59,26,41,58]
insertion_sort_nonincreasing(A)
print(A)
