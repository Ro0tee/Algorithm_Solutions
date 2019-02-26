'''
Problem:
    Consider sorting n numbers in an array A by first finding the smallest element of A and exchanging it with the element in A[1]. Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n−1 elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariants does this algorithm maintain? Why does it need to run for only the first n−1 elements, rather than for all n elements? Give the best-case and the worst-case running times of selection sort in Θ-notation.

Pseudocode

SELECTION-SORT(A)
tmp = 0 
for min = j = 1 to A.length -1
    for i = j+1 to A.length
        if A[i]<A[min]
            min = i
    tmp = A[j]
    A[j] = A[min]
    A[min] = tmp

'''

def selection_sort(A):
    tmp = 0
    for j in range(0,len(A)-1):
        min = j
        for i in range(j+1,len(A)):
            if(A[i]<A[min]):
                min = i
        tmp = A[j]
        A[j] = A[min]
        A[min] = tmp
    

#test
A = [31,41,59,26,41,58]
selection_sort(A)
print(A)