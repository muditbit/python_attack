def split(a):
    c =[]
    for i in range(len(a)):
        b = a[i]
        c.append(b +(sum(a)-b)/(len(a)-1))

    return max(c)


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    arr = list(map(int,input().split()))
    res = split(arr)
    print(res)
