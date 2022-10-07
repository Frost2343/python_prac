PROGRAM:

n=int(input("enter no. of students:"))
lst1=list()
for i in range(0,n):
    r=int(input("enter roll number:"))
    name=input("enter name:")
    m1=int(input("enter m1:"))
    m2=int(input("enter m2:"))
    m3=int(input("enter m3:"))
    l1=[r,name,m1,m2,m3]
    tup=tuple(l1)
    lst1.append(tup)
    tup=tuple(lst1)
print("1.display all\n2.python data\n3.sort\n4.add\n5.remove\n6.exit.")
while True:
    c=int(input("enter choice:"))
    if(c==1):
        for t in tup:
            print(t)
    elif(c==2):
        for t in tup:
            if "python" in t:
                print("roll number:",t[0])
                print("marks for subject 1:",t[2])
                print("marks for subject 2:",t[3])
                print("marks for subject 3:",t[4])
    elif(c==3):
        print(sorted(tup,key=lambda x:x[1]))
    elif(c==4):
        lst=list()
        for i in tup:
            lst.append(i)
        l1=lst[:1]
        l2=lst[1:]
        r=int(input("enter roll number:"))
        name=input("enter name:")
        m1=int(input("enter m1:"))
        m2=int(input("enter m2:"))
        m3=int(input("enter m3:"))
        t1=(r,name,m1,m2,m3)
        lst.clear()
        for i in l1:
            lst.append(i)
        lst.append(t1)
        for i in l2:
            lst.append(i)
        print(lst)
    elif(c==5):
        lst=list()
        for i in tup:
            lst.append(i)
        l1=lst[:1]
        l2=lst[2:]
        lst.clear()
        for i in l1:
            lst.append(i)
        for i in l2:
            lst.append(i)
        print(lst)
    elif(c==6):
        break
    else:
        print("enter valid choice")


OUTPUT:

enter no. of students:3
enter roll number:1
enter name:python
enter m1:23
enter m2:45
enter m3:56
enter roll number:2
enter name:arsh
enter m1:45
enter m2:67
enter m3:78
enter roll number:3
enter name:bot
enter m1:3
enter m2:4
enter m3:5
1.display all
2.python data
3.sort
4.add
5.remove
6.exit.
enter choice:1
(1, 'python', 23, 45, 56)
(2, 'arsh', 45, 67, 78)
(3, 'bot', 3, 4, 5)
enter choice:2
roll number: 1
marks for subject 1: 23
marks for subject 2: 45
marks for subject 3: 56
enter choice:3
[(2, 'arsh', 45, 67, 78), (3, 'bot', 3, 4, 5), (1, 'python', 23, 45, 56)]
enter choice:4
enter roll number:6
enter name:tom
enter m1:2
enter m2:4
enter m3:6
[(1, 'python', 23, 45, 56), (6, 'tom', 2, 4, 6), (2, 'arsh', 45, 67, 78), (3, 'bot', 3, 4, 5)]
enter choice:5
[(1, 'python', 23, 45, 56), (3, 'bot', 3, 4, 5)]
enter choice:6

