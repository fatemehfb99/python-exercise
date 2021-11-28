second=int(input("please enter second : "))
hour=second//3600
second=second%3600
minute=second//60
second=second%60
print(str(hour)+" : "+str(minute)+" : "+str(second))