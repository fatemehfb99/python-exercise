import random
true_char=[]
words=["apple","banana","kiwi","orange"]
word=random.choice(words)
score=len(word)
for i in range (len(word)):
    true_char.append("___   ")
while True:
    print(true_char)
    f=0
    char=input("please enter character : ")
    for i in range (len(word)):
        if word[i]==char:
            score=score+1
            true_char[i]=char
            f=1
    if f==0:
        score=score-1
    if (score==2*len(word)):
        print("* * *wwwiiinnn* * *")
        break
    elif(score==0):
        print("* * *game over* * *")
        break