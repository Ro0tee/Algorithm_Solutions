'''
Pseudocode

BINARY_SEARCH(A,v,low,high)
mid = (low+high)//2
if mid>0 and mid<high+1
    if A[mid] == v
        return mid
    else if A[mid] > v
        low = mid + 1
    else
        high = mid - 1
    BINARY_SEARCH(A,v,low,high)
else return NIL

'''

def binary_search(A,v,low,high):
    mid = (low+high)//2
    if(mid >=0 and mid < high):
        if(A[mid] == v):
            return mid
        elif(A[mid] > v):
            low = mid+1
        else:
            high = mid-1
        binary_search(A,v,low,high)
    return None
    

#test
A = [26,31,41,41,58,59]
v = 15
print(binary_search(A,v,0,len(A)-1))
v = 41
print(binary_search(A,v,0,len(A)-1))