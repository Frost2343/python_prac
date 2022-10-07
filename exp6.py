PROGRAM:

print("1.create\n2.concatenate\n3.search\n4.mapping\n5.exit")
while True:
    c=int(input("enter choice:"))
    if c==1:
   	 l1=[int(x) for x in input("enter keys of dict:").split()]
   	 l2=[x for x in input("enter values of dict:").split()]
   	 z1=zip(l1,l2)
   	 d1=dict(z1)
   	 print("dict 1:",d1)
   	 l3=[int(x) for x in input("enter keys of dict:").split()]
   	 l4=[x for x in input("enter values of dict:").split()]
   	 z2=zip(l3,l4)
   	 d2=dict(z2)
   	 print("dict 2:",d2)
    elif c==2:
   	 d1.update(d2)
   	 print("dict:",d1)
   	 s=int(input("enter the key to be deleted:"))
   	 d1.pop(s)
   	 print("dict:",d1)
    elif c==3:
   	 key=d1.keys()
   	 s=int(input("enter key to be searched:"))
   	 for i in key:
   		 if s==i:
   			 print("key:",i,"value:",d1[i])
    elif c==4:
   	 c1=[x for x in input("enter city names:").split()]
   	 p1=[int(x) for x in input("enter zipcodes:").split()]
   	 z3=zip(c1,p1)
   	 d3=dict(z3)
   	 print("mapped dictionary:",d3)
    elif c==5:
   	 exit(0)
    else:
   	 print("enter valid choice:")

OUTPUT:

1.create
2.concatenate
3.search
4.mapping
5.exit
enter choice:1
enter keys of dict:1 2 3
enter values of dict:a s d
dict 1: {1: 'a', 2: 's', 3: 'd'}
enter keys of dict:4 5 6
enter values of dict:q w e
dict 2: {4: 'q', 5: 'w', 6: 'e'}
enter choice:2
dict: {1: 'a', 2: 's', 3: 'd', 4: 'q', 5: 'w', 6: 'e'}
enter the key to be deleted:3
dict: {1: 'a', 2: 's', 4: 'q', 5: 'w', 6: 'e'}
enter choice:3
enter key to be searched:5
key: 5 value: w
enter choice:4
enter city names:mumbai delhi chennai
enter zipcodes:400701 400030 400908
mapped dictionary: {'mumbai': 400701, 'delhi': 400030, 'chennai': 400908}
enter choice:5



