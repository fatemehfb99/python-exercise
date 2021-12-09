import random
arr=["stone","paper","scissors"]
s1=0
s2=0
n=int(input("times : "))
for i in range (n):
    p1=random.choice(arr)
    p2=input("please enter your move : ")
    if (p1=="pepar" and p2=="stone") or (p1=="scissors" and p2=="paper") or (p1=="stone" and p2=="scissors"):
        s1=s1+1
    elif (p1=="stone" and p2=="pepar") or (p1=="paper" and p2=="scissors") or (p1=="scissors" and p2=="stone"):
        s2=s2+1
if s1>s2:
    print("player 1")
elif s2>s1:
    print("player 2")
else:
    print("equal")