class C:
    def __init__(self,value):
        if value!=0:
            self.ctvalue=value
        else:
            self.ctvalue=0
    def __str__(self):
        return f'{self.ctvalue}'
    def m1(self):
        return self.ctvalue
    def m2(self):
        self.ctvalue+=1
    def m3(self):
        self.ctvalue-=1
    def m4(self,n):
        self.ctvalue+=n

c=C(5)
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1())
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())
c.__str__()