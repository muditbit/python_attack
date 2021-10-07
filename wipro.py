n = int(input())
arr = list(map(int,input().split()))

count =  len([i for i in arr if i>0])
print(count)
