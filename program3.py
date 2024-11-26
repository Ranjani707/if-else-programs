#3)write a program to find max among given 4 number

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c and d>c:
    print(a,'a is max')
elif b>c and b>d:
    print(b,'b is max')
elif c>d:
    print(c,'c is max')
else:
    print(d,'d is max')
    