while(True):
    c=1
    n=int(input("enter number:"))
    s=input("enter string:")
    l=len(s)
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial of %d is %d." %(n,f))
    c=0
    for i in range(0,l-1):
        if(s[i]==s[l-1]):
           i=i+1
           l=l-1
        else:
            c=c+1

    if(c==0):
        print("%s is a palindrome!" %(s))
    else:
        print("%s is not a palindrome!" %(s))
    print("More iterations? Press(0/1)")
    c=int(input("enter choice:"))
    if(c==0):
        print("execution completed.")
        exit(0);

"""
OUTPUT:

enter number:3
enter string:harry
factorial of 3 is 6.
harry is not a palindrome!
More iterations? Press(0/1)
enter choice:1
enter number:4
enter string:racecar
factorial of 4 is 24.
racecar is a palindrome!
More iterations? Press(0/1)
enter choice:0
execution completed.

"""

        
