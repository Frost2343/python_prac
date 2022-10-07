PROGRAM:

s1=set(i for i in input("enter string 1:"))
s2=set(i for i in input("enter string 2:"))
print("1.intersection\n2.difference\n3.union\n4.symmetric_diff")
print("set1:",s1,"set2:",s2)
while True:
    c=int(input("enter your choice:"))
    if c==1:
        print(s1.intersection(s2))
    elif c==2:
        print(s1.difference(s2))
    elif c==3:
        print(s1.union(s2))
    elif c==4:
        print(s1.symmetric_difference(s2))
    elif c==5:
        print("executed.")
        break
    else:
        print("enter valid choice.")

OUTPUT:

enter string 1:arsh
enter string 2:ayaan
1.intersection
2.difference
3.union
4.symmetric_diff
set1: {'s', 'a', 'r', 'h'} set2: {'a', 'n', 'y'}
enter your choice:1
{'a'}
enter your choice:2
{'s', 'h', 'r'}
enter your choice:3
{'s', 'r', 'h', 'y', 'a', 'n'}
enter your choice:4
{'h', 's', 'r', 'y', 'n'}
enter your choice:5
executed.

