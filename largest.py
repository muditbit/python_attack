

a=[]
n= int(input('Enter the length of List:'))
print('Enter the Elements of List:\n')
for i in range(0,n):
    item =int(input())
    a.append(item)


print('User Entered :',a)
print("Largest value in the given list is:",max(a))
'''print('Finding the largest no.....')
sort(a,n)
print('Largest no. in the given list is :',a[n-1])'''
