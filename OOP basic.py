class Basic:
    def __init__(self):
        self.basic = input()
        
        
    def compare(self,other):
        if self.basic == other.basic:
            return True
        else:
            return False
class Basic2(Basic):
    def __init__(self,basic):
        self.basic = int(basic)

    def add(self,other):
        sumation = self.basic + other.basic
        return sumation


n1 = int(input())
n2 = int(input())

n1 = Basic2(n1)
n2 = Basic2(n2)

print(n1.compare(n2))

n3= Basic()
n4 = Basic()

print(n3.add(n4))




    
