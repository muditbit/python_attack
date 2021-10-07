def monitor(arr,n):
    s=list(set(arr))
    s.sort()
    maxi =0
    for i in range(len(s)-1,0,-1):
        h1 = arr.count(s[i])
        for j in range(0,i):
            h2 = arr.count(s[j])
            maxi =max(maxi,h1-h2)

    if maxi >0:
        return maxi
    else:
        return -1

for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(monitor(arr,n))

