n = int(input("Enter the range:"))
c=0
while c!=n:
    for i in range(1,n+1,1):
        if i==1 or i==0:
            continue

        flag =1;

        for j in range(2,((i//2)+1),1):
            if i %j==0:
                flag=0;
                break;

        if flag == 1:
            print(i,end=',')

    c=c+1
