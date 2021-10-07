def long(str):
    n = len(str)
    start = 0
    end = n-1
    xPos =0
    yPos =0

    while(True):
        if str[start]== 'a':
            xPos = start
            break
        start += 1



    while(True):
        if str[end]=='z':
            yPos= end
            break

        end -= 1

    length = (yPos-xPos) + 1

    print(length)


string = input()

long(string.lower())
