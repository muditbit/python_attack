class X:
    def __init__(self):
         self.a = 10
         self._b = 20
    def getB(self):
         return self._b

x = X()
x._b = 60
print(x.getB())
