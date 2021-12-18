def read():
    wrd=[]
    fl=open('translate.txt','r')
    file=fl.read()
    words=file.split('\n')
    for i in range(0,len(words)-1,2):
        wrd.append({'english':words[i],'persian':words[i+1]})
    return wrd
#print(read())

tr=read()

def menu():
    mu=int(input("1 . translate english to persian\n2 . translate persian to english\n3 . add word\n4 . exit\nplease enter a number : "))
    return mu

def translate_PtoE():
    keyword=input('enter a word : ')
    for t in tr:
        if keyword==t['persian']:
            print(t['english'])
    else:
        print('not find')

def translate_EtoP():
    keyword=input('enter a word : ')
    for t in tr:
        if keyword==t['english']:
            print(t['persian'])
    else:
        print('not find')

def add():
    keyword1=input('english : ')
    keyword2=input('persian : ')
    for t in tr:
        if keyword1==t['english'] or keyword2==t['persian']:
            print('this word exist')
            return
    tr.append=[{'english':keyword1,'persian':keyword2}]

def exiit():
    finish=(input("do you want to save information ? yes / no "))
    if finish=='yes':
        fl=open('translate.txt','w')
        for t in tr:
            fl.write(t['english']+','+t['persian']+'\n')
        fl.close()
        exit()
    else:
        exit()

while True:
    user=menu()
    if user==1:
        translate_EtoP()
    elif user==2:
        translate_PtoE()
    elif user==3:
        add()
    elif user==4:
        exiit()
    else:
        print('wrong number!!!')