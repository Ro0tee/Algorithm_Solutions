'''
Problem: 
    Consider the searching problem:

    Input: A sequence of n numbers A=⟨a1,a2,…,an⟩ and a value ν.

    Output: And index i such that ν=A[i] or the special value NIL if ν does not appear in A

    Write the pseudocode for linear search, which scans through the sequence, looking for ν. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

Pseudocode

SEARCH(A,v)
for j = 1 to A.length
    if A[j] == v
        then return j
return NIL

'''

def search(A,v):
    for j in range(0,len(A)):
        if(A[j] == v):
            return j
    return None

#test
A = [31,41,59,26,41,58]
v = 15
print(search(A,v))
v = 26
print(search(A,v))
