arr=[]
n=int(input("please enter number : "))
for i in range (n):
    a=int(input("please enter a number : "))
    arr.append(a)
print(arr)
for i in range (n-1):
    for j in range (n-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)