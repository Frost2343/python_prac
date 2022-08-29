import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
print("before swapping\na=%d b=%d" %(a,b))
temp=a
a=b
b=temp
print("after swapping\na=%d b=%d" %(a,b))
print("now checking whether a is postive, negative or zero.")

if(a==0):
    print("zero.")
elif(a>0):
    print("positive.")
else:
    print("negative.")
print("now checking whether b is postive, negative or zero.")

if(b==0):
    print("zero.")
elif(b>0):
    print("positive.")
else:
    print("negative.")
"""
OUTPUT:

python3 exp1.py 2 5
before swapping
a=2 b=5
after swapping
a=5 b=2
now checking whether a is postive, negative or zero.
positive.
now checking whether b is postive, negative or zero.
positive.
"""
