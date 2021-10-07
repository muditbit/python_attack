base = int(input('Enter the base no:'))
exponent = int(input('Enter the exponent no:'))

def power(base,exp):
    for i in range(exp+1):
        print(base,'to the',i,'th power is :',base**i)
    return

power(base,exponent)
