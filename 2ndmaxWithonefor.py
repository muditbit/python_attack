arr = list(map(int,input().split()))
n = len(arr)

first = arr[0]
second =0
for i in range(1,n):
    if arr[i]>first:
        second = first
        first = arr[i]

print(first)
print(second)
