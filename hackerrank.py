n = int(input())
c = []
d = []
for i in range(n):
    a=[]
    for j in range(2):
        if j==0:
            
            a.append(input())
        else:
            score = float(input())
            a.append(score)
            d.append(score)
    c.append(a)
d.sort()
c.sort()
d = list(dict.fromkeys(d))
for i in range(0,n):
    if d[1]==c[i][1]:
        print(c[i][0])
