'''
Problem:
    Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n+1)-element array C. State the problem formally and write pseudocode for adding the two integers.

Pseudocode

ADD(A,B)
C = new integer[A.length+1]
carry = 0
j = A.length
while j>0:
    C[j+1] = (A[j] + B[j]+carry)%2
    carry = (A[j] + B[j] + carry)/2
    j-=1
C[j+1] = carry
return C

'''

def add_bin(A,B):
    C = [0 for i in range(len(A)+1)]
    carry = 0
    for j in range(len(A)-1,-1,-1):
        C[j+1] = (A[j] + B[j] + carry)%2
        carry = (A[j] + B[j] + carry)//2
    C[j] = carry
    return C

#test
A = [1,1,1,1]
B = [1,1,0,1]
print(add_bin(A,B))