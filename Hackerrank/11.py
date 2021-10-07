n = int(input())
s = set(map(int, input().split()))
comnd = int(input())
for i in range(comnd):
    item = input()
    if 'pop' in item:
        
        s.pop()
    elif 'remove' in item:
        li = list(item.split(" "))
        x = li[1]
        x = int(x)
        s.remove(x)
    elif 'discard' in item:
        li = list(item.split(" "))
        x = li[1]
        x = int(x)
        
        s.discard(x)


print(s)
