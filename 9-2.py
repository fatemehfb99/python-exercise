def number(num,digit):
    c=0
    while num!=0:
        r=num%10
        if r==digit:
            c=c+1
        num=num//10
    return c

n=int(input("please enter a number : "))
m=int(input("please enter a digit : "))
print(number(n,m))