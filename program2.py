#2) write a program to find max among given 3 number

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a,'a is max')
elif b>c:
    print(b,'b is max')
else:
    print(c,'c is max')