PROGRAM:
class A:
    def __init__(self,a):
   	 self.vara=a
    def dis(self):
   	 print(self.vara,"this is class A")
    def mod(self,a):
   	 self.vara=a

class B:
    def __init__(self,b):
   	 self.varb=b
    def dis(self):
   	 print(self.varb,"this is class B")
    def mod(self,b):
   	 self.varb=b
   	 
class C:
    def __init__(self,a,b,c):
   	 A.__init__(self,a)
   	 B.__init__(self,b)
   	 self.varc=c
    def dis(self):
   	 A.dis(self)
   	 B.dis(self)
   	 print(self.varc,"this is class C")
    def mod(self,a,b,c):
   	 A.mod(self,a)
   	 B.mod(self,b)
   	 self.varc=c

x=C("hi","hello","hey")
x.dis()
x.mod("one","two","three")
x.dis()

/*
OUTPUT:
hi this is class A
hello this is class B
hey this is class C
one this is class A
two this is class B
three this is class C
*/

