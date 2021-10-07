def GCD(arr):
    result = arr[0]
    for x in arr[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result
    
def update(arr,i,x):
    arr[i-1] = arr[i-1] * x
    return arr

n, q = map(int,input().split())
arr = list(map(int, input().split()))
for _ in range(q):
    i,x =map(int,input().split())
    res = update(arr,i,x)
    final = GCD(res)
    print(final)
