'''Question :- '''

n = int(input())
t= int(input())
l = [i for i in range(1,n+1)]
q = t//(n-1)
k = t%(n-1)
if q%2==0:
    if k==0:
        print(l[k+1],l[k])
    else:
        
        print(l[k-1],l[k])
else:
    arr = l[::-1]
    if k==0:
        print(arr[k+1],arr[k])
    else:
        
        print(arr[k-2],arr[k])