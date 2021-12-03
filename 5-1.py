n=int(input("please enter number : "))
for i in range (n):
    a=int(input("please enter a number : "))
    fact=1
    for j in range (1,a+1,1):
        fact=fact*j
    print(str(a)+" ! = "+str(fact))