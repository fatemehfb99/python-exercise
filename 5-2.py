arr=[]
n=int(input("please enter size of array : "))
while len(arr)!=n:
    a=int(input("please enter a number : "))
    if a%2==0:
        arr.append(a)
print(arr)