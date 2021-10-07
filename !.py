def factors(num):
    a=[]
    for i in range(1,num+1):
        if num%i == 0:
            a.append(i)

    return a

num = int(input())
res = factors(num)
print(res)  

mid = len(res)//2
print(res[mid])

n = num//res[mid]

if n<res[mid]:
    res[mid] = str(res[mid])
    print(len(res[mid]))
else:
    n = str(n)
    print(len(n))
