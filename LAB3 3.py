#0 1 1 2 3 5 8
n=int(input("Enter a number: "))
a=0
b=1
count=1
print(a)
print(b)
while(count<=n-2):
    c=a+b
    print(c)
    count=count+1
    a=b
    b=c