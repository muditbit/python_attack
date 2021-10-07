n = int(input('enter'))
ar =[]
for i in range(n):
    item = str(input('enter element'))
    ar.append(item)
def count_valley(n,ar):
    l=0
    c=0
    for i in range(len(ar)):
        if ar[i]=='U':
            l=l+1
            if l ==0:
                c=c+1
        else:
            l=l-1
            if l == 0:
                c=c+1
    if ar[0]=='U':
        
        print(c-1)
    else:
        print(c)

count_valley(n,ar)
            
