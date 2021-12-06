import random
c=0
b=0
words=["apple","banana","kiwi","orange"]
word=random.choice(words)
for i in range (len(word)):
    print("___",end="  ")
print()
while True:
    a=input("please enter character : ")
    for i in range (len(word)):
        if a==word[i]:
            for k in range (i):
                print("___",end="  ")
            print(a,end="  ")
            for k in range (i+1,len(word)):
                print("___",end="  ")
            b=b+1
        else:
            c=c+1
        if c==len(word):
            print("* * *game over* * *")
            break
        elif b==len(word):
            print("* * *wwwwin* * *")
            break
    if c==len(word) or b==len(word):
        break