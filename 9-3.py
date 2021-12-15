arr=[]
n=int(input("please enter a number : "))
for i in range(n):
    x=int(input("number : "))
    arr.append(x)
for i in range (n):
    for j in range(arr[i]):
        print("*",end="  ")
    print()
print(arr)