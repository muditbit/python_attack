arr = list(map(int,input().split()))
n = len(arr)

s = arr[0]
for i in range(1,n):
    if arr[i]>s:
        s = arr[i]

print(s)
