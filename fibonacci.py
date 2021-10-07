a=int(input('Enter The first No of the series:'))
b=int(input('Enter the second no. of the series:'))

n =  int(input('Enter the terms needed:'))
print(a,b,end=" ")
while n-2:
    c= a+b
    a=b
    b=c
    print(c,end = " ")
    n=n-1
