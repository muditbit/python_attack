def sqr_root(n,l):
    x = n
    count = 0
    while(1):
        count += 1

        root = 0.5*(x + (n/x))

        if(abs(root -x)< 1):
            break

        x =root

    return root


n= int(input('Enter the desired no.: '))
l = 0.00001

print('Square root of given desired no',n,'is :',sqr_root(n,l))
