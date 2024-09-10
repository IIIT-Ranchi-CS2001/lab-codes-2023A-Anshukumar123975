s=input("Enter a  string")
ch=input("Enter the character")
count=0
for i in s:
    if ch==i:
        count=count+1
print("The number of occurences of the selected character is: ",count)
    