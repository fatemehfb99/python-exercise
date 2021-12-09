c=0
s=input("please enter a sentence : ")
for i in range (len(s)):
    if (s[i]<='Z' and s[i]>='A') or (s[i]<='z' and s[i]>='a'):
        c=c+1
print(c)