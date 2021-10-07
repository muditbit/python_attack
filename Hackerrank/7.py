str1 = str(input())
l =[]
def convert(str):
    li=list(str.split(" "))
    return li
x=[]
l = convert(str1)
for i in range(len(l)):
    x.append(l[i].capitalize())
    
#print(x)


def listtostring(list):
    str2 =" "
    return str2.join(list)

print(listtostring(x))
