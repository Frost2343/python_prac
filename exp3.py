
PROGRAM:

l1=[int(i) for i in input("Enter odd elments:").split()]
l2=[int(i) for i in input("Enter even elments:").split()]
print("list1:",l1,"\nlist2:",l2)
while True:
    print("\n1.to sort\n2.to concatenate\n3.to update index 0 and pop mid\n4.to find min and max\n5.to check python present.")
    c = int(input("enter choice:"))
    if c==1:
   	 l1.sort()
   	 l2.sort()
   	 print("after sorting:\nlist1:",l1,"\nlist2:",l2)
    elif c==2:
   	 l1.extend(l2)
   	 l1.sort()
   	 print("list after merging:",l1)
    elif c==3:
   	 l1[0]=int(input("enter elment at index 0:"))
   	 print("list after updating:",l1)
   	 mid=len(l1)//2
   	 l1.pop(mid)
   	 print("list after removing mid:",l1)
    elif c==4:
   	 print("max=",max(l1),"min=",min(l1))
    elif c==5:
   	 n=int(input("enter no. of names:"))
   	 name=[n for n in input("enter names:").split(',')]
   	 for n in name:
   		 l1.append(n)
   	 print("updated list:",l1)
   	 if l1.count("py")>0:
   		 print("python present.")
   	 else:
   		 print("python absent.")
    else:
   	 print("executed.")
   	 break

OUTPUT:

Enter odd elments:7 5 3
Enter even elments:6 4 2
list1: [7, 5, 3]
list2: [6, 4, 2]

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:1
after sorting:
list1: [3, 5, 7]
list2: [2, 4, 6]

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:2
list after merging: [2, 3, 4, 5, 6, 7]

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:3
enter elment at index 0:8
list after updating: [8, 3, 4, 5, 6, 7]
list after removing mid: [8, 3, 4, 6, 7]

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:4
max= 8 min= 3

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:5
enter no. of names:2
enter names:hello
updated list: [8, 3, 4, 6, 7, 'hello']
python absent.

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:5
enter no. of names:2
enter names:arsh,py
updated list: [8, 3, 4, 6, 7, 'hello', 'arsh', 'py']
python present.

1.to sort
2.to concatenate
3.to update index 0 and pop mid
4.to find min and max
5.to check python present.
enter choice:6
executed.

   	 


