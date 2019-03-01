'''
Honer's rule
Pseudocode
ELements in A is sorted by degree in increasing
Honer_rule(A,x)
y=0
for j=A.length downto 1
    y=A[j]+x*y

Evaluate each term of poly
Pseudocode
ELements in A is sorted by degree increasingly
solution(A,x)
y=0
n=1
for j=1 to A.length
    y=A[j]*n+y
    n=n*x

'''
#Honer_rule
def honer_rule(A,x):
    y=0
    for j in range(len(A)-1,-1,-1):
        y=A[j]+x*y
    return y

#another solution
def solution(A,x):
    y=0
    n=1
    for j in range(0,len(A)):
        y=A[j]*n+y
        n=n*x
    return y
