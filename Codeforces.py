n = int(input())


a= []
b=[]
for i in range(n):

    sticks = int(input())
    diamond = int(input())
    a.append(sticks)
    b.append(diamond)

for i in range(n):
    c=0
    d=0
    e=0
    f=0
    if (a[i]>=b[i]):
        if(b[i]==0):
            print(c)
        else:
            d = a[i]//2
            e = b[i]
            if(d <b[i]-2):
                f=d-1
                e = b[i]-(d-1)
                e = e//2
                if(e<2):
                    print(e+f)
                else:
                    print(f+2)
            else:
                print(d)

    elif(b[i]>a[i]):
        if(a[i]==0):
            print(c)
        else:
            e = b[i]//2
            d = a[i]
            if(e <a[i]-2):
                f=e-1
                d = a[i]-(d-1)
                d = d//2
                if(d<2):
                    print(d+f)
                else:
                    print(f+2)
            else:
                print(e)
