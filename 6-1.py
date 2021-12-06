import random
n=int(input("please enter n : "))
m=int(input("please enter m : "))
arr=[[None for i in range (m)]for j in range (n)]
for i in range (n):
    for j in range (m):
        arr[i][j]=random.randint(10,99)
for i in range (n):
    for j in range (m):
        print(arr[i][j],end="\t")
    print()