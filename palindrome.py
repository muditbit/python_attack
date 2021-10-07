
    

innum = int(input())
num1= 0
num2= 0

while num1==0:
    num1 = innum-1
    temp = num1
    reverse = 0
   
    while (num1>0):
        digit = num1%10
        reverse = reverse*10+digit
        num1 = num1//10
    if temp==reverse:
        num1 = temp
        break
    else:
        num1 =num1-1
    


while True:
    num2 = innum+1
    temp = num2
    reverse = 0
    while num2>0:
        digit = num2%10
        reverse = reverse*10 + digit
        num2 = num2//10
    if temp==reverse:
        num2 = temp
        break
    else:
        num2 +=1


print(num1)
print(num2)
