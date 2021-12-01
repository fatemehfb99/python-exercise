a=int(input("please enter first number : "))
b=int(input("please enter second number : "))
i=1
j=1
sum1=a
sum2=b
while sum1!=sum2:
    if sum1<sum2:
        i=i+1
        sum1=a*i
    elif sum1>sum2:
        j=j+1
        sum2=b*j
    if sum1==sum2:
        print(sum1)