import math
num1=int(input("please enter first number : "))
op=input("please enter operation : ")
if op=="+" or op=="-" or op=="*" or op=="/" or op=="pow":
    num2=int(input("please enter second number : "))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
elif op=="sin":
    print(math.sin(num1))
elif op=="cos":
    print(math.cos(num1))
elif op=="tan":
    print(math.tan(num1))
elif op=="pow":
    print(math.pow(num1,num2))
elif op=="sqrt":
    print(math.sqrt(num1))