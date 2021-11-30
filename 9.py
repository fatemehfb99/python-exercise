weight=float(input("please enter weight : "))
stature=float(input("please enter stature : "))
bmi=weight/stature**2
if bmi<18.5:
    print("under weight")
elif bmi>=18.5 and bmi<25:
    print("normal")
elif bmi>=25 and bmi<30:
    print("over weight")
elif bmi>=30 and bmi<=35:
    print("obese")
else:
    print("extremely obese")