a=str(input())
query =str(input())
count =0
for  i  in range(len(a)):
    if a[i:i+len(query)]==query:
        count+=1
    else:
        count = count
print(count)

