s=input("Enter the string")
b=0
for i in s:
    if i.isalnum()==0:
        b=1
        break
if b==1:
    print("False")
else:
    print("True")        