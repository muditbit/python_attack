if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        
        d = list(map(str,input().split()))
        
        
        if d[0]=='append':
            l.append(int(d[1]))
            d = []
        elif d[0]== 'insert':
            l.insert(int(d[1]), int(d[2]))
            d =[]
        elif d[0] == 'remove':
            l.remove(int(d[1]))
            d =[]
        elif d[0]=='sort':
            l.sort()
            d = []
        elif d[0] == 'pop':
            l.pop()
            d = []
        elif d[0]=='reverse':
            l.reverse()
            d=[]
            
        elif d[0]=='print':
            print(l)
            d=[]
