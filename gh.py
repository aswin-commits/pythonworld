n=input("enter a string)")
i=len(n)
while i>0:
    if(i==len(n)):
        if(n[0]==n[i]):
            n[i]='$'
            i=i-1
    elif(n[0]==n[i-1]):
            n[i-1]='$'
            i=i-1

