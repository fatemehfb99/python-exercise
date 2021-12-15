import time
import random
from colorama import Fore
def check():
    p=None
    for i in range (3):
        if arr[i][0]==arr[i][1]==arr[i][2] and arr[i][0]!="_":
            p=arr[i][0]
            break
    for j in range (3):
        if arr[0][j]==arr[1][j]==arr[2][j] and arr[0][j]!="_":
            p=arr[0][j]
            break
    if arr[0][0]==arr[1][1]==arr[2][2] and arr[0][0]!="_":
        p=arr[0][0]
    if arr[0][2]==arr[1][1]==arr[2][0] and arr[0][2]!="_":
        p=arr[0][2]
    return p
start=time.time()
arr=[["_" for i in range (3)]for j in range (3)]
for i in range (3):
    for j in range (3):
        if arr[i][j]=="O":
            print(Fore.GREEN+str(arr[i][j]),end="  ")
        elif arr[i][j]=="X":
            print(Fore.YELLOW+str(arr[i][j]),end="  ")
        else:
            print(Fore.WHITE+str(arr[i][j]),end="  ")
    print()
print(Fore.RESET)
flag=int(input("if you want play alone enter 1 else enter 2 : "))
c=0
while True:
    while True:
        if flag==2:
            row=int(input("row O : "))
            column=int(input("column O : "))
            if row>=0 and row<3 and column>=0 and column<3 and arr[row][column]=="_":
                c=c+1
                arr[row][column]="O"
                break
        elif flag==1:
            row=random.randint(0,2)
            column=random.randint(0,2)
            if arr[row][column]=="_":
                c=c+1
                arr[row][column]="O"
                break
        print("try again")
    for i in range (3):
        for j in range (3):
            if arr[i][j]=="O":
                print(Fore.GREEN+str(arr[i][j]),end="  ")
            elif arr[i][j]=="X":
                print(Fore.YELLOW+str(arr[i][j]),end="  ")
            else:
                print(Fore.WHITE+str(arr[i][j]),end="  ")
        print()
    print(Fore.RESET)
    if c>3:
        if check()=='X':
            print("player X is winner")
            break
        elif check()=="O":
            print("player O is winner")
            break
    if (c==9):
        print("equal")
        break
    while True:
        row=int(input("row X : "))
        column=int(input("column X : "))
        if row>=0 and row<3 and column>=0 and column<3 and arr[row][column]=="_":
            c=c+1
            arr[row][column]="X"
            break
        print("try again")
    for i in range (3):
        for j in range (3):
            if arr[i][j]=="O":
                print(Fore.GREEN+str(arr[i][j]),end="  ")
            elif arr[i][j]=="X":
                print(Fore.YELLOW+str(arr[i][j]),end="  ")
            else:
                print(Fore.WHITE+str(arr[i][j]),end="  ")
        print()
    print(Fore.RESET)
    if c>3:
        if check()=='X':
            print("player X is winner")
            break
        elif check()=="O":
            print("player O is winner")
            break
    if (c==9):
        print("equal")
        break
print("time : "+str(time.time()-start))