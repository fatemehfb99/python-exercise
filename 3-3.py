a=int(input("please enter 5 numbers : "))
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a>b:
    temp=a
    a=b
    b=temp
if a>c:
    temp=a
    a=c
    c=temp
if a>d:
    temp=a
    a=d
    d=temp
if a>e:
    temp=a
    a=e
    e=temp
if b>c:
    temp=b
    b=c
    c=temp
if b>d:
    temp=b
    b=d
    d=temp
if b>e:
    temp=b
    b=e
    e=temp
if c>d:
    temp=c
    c=d
    d=temp
if c>e:
    temp=c
    c=e
    e=temp
if d>e:
    temp=d
    d=e
    e=temp
print("sort : ")
print(a)
print(b)
print(c)
print(d)
print(e)