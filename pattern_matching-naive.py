d = {"a":1,"b":2,"c":3,"d":4,"e":5}

def robin(string,pattern):
    a =[]
    for i in range(len(string)-len(pattern)+1):
        if string[i]== pattern[0]:
            flag=0
            for j in range(1,len(pattern)):
                
                if string[i+j]==pattern[j]:
                    flag += 1
                else:
                    
                    break
            if flag == len(pattern)-1:
                print(i, end=" ")



robin("abcbdbceabcbd","abc")
    
