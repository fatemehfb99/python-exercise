def read_db():
    products=[]
    fl=open('store.csv','r')
    whole=fl.read()
    rows=whole.split('\n')
    for i in range(len(rows)-1):
        info=rows[i].split(',')
        products.append({'id':info[0],'name':info[1],'price':info[2],'count':info[3]})
    # print(rows)
    # print(whole)
    return products

pr=read_db()
fac=0

def menu():
    mu=int(input("1 . add\n2 . remove\n3 . buy\n4 . edit\n5 . search\n6 . show all\n7 . exit\nplease enter a number : "))
    return mu

def add():
    id=input('enter id : ')
    for p in pr:
        if id==p['id']:
            print('this product exist')
            return
    name=input('enter name : ')
    price=input('enter price : ')
    count=input('enter count : ')
    pr.append({'id':id,'name':name,'price':price,'count':count})

def remove():
    keyword=input('enter something : ')
    for p in pr:
        if keyword==p['id'] or keyword==p['name'] or keyword==p['price'] or keyword==p['count']:
            pr.remove(p)

def buy():
    id=input('enter id : ')
    count=int(input('enter count : '))
    for p in pr:
        if id==p['id']:
            count1=int(p['count'])
            price1=int(p['price'])
            count1=count1-count
            fac=fac+price1*count1
            p['count']=str(count1)
    else:
        print('not find')

def edit():
    id=input('enter id : ')
    for p in pr:
        if id==p['id']:
            p['name']=input("enter name : ")
            p['price']=input('enter price : ')
            p['count']=input('enter count : ')
            break
    else:
        print("not find!!!")
    
def search():
    keyword=input('enter something : ')
    for p in pr:
        if keyword==p['id'] or keyword==p['name'] or keyword==p['price'] or keyword==p['count']:
            print(p)

def show():
    id=input('enter id : ')
    for p in pr:
        if id==p['id']:
            print(p)

def exiit():
    finish=(input("do you want to save information ? yes / no "))
    if finish=='yes':
        fl=open('store.csv','w')
        for p in pr:
            fl.write(p['id']+','+p['name']+','+p['price']+','+p['count']+'\n')
        fl.close()
        exit()
    else:
        exit()

while True:
    user=menu()
    if user==1:
        add()
    elif user==2:
        remove()
    elif user==3:
        buy()
    elif user==4:
        edit()
    elif user==5:
        search()
    elif user==6:
        show()
    elif user==7:
        exiit()
    else:
        print("wrong number!!!")
