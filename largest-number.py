#Find the largest number
a=int(input("enter the 1st value"))
b=int(input("enter the 2nd value"))
c=int(input("enter the 3rd value"))
if a!=b!=c:
    print("your entered numbers are")
    if b<a>c:
        print("a is greater ")
        if c<b>a:
            print("b is greater")
            if a<c>b:
                print("c is greater ")
else:
    print("you entered similar numbers")
    