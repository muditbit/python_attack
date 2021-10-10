'''Question :- There are n friends
 standing in a line, each numbered from 1
through n inclusive. The first one, 
friend 1, holds a baton. 
Each second, the baton is passed to 
the next friend in line. 
Once it reaches the end of the line, 
the direction of passing is reversed 
and passing continues. 
Determine who will pass and who 
will receive the baton at a given time.'''

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
