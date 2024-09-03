import math
a=12
b=13
c=14
d=math.pow(b,2) - 4*a*c
r1=0
r2=0
if(d==0):
    r1=((-1*b))/(2*a)
    r2=r1
elif(d>0):
    r1 = ((-1*b) + math.sqrt(d))/(2*a)
    r2 = ((-1*b) - math.sqrt(d))/(2*a)
else:
    real_part = ((-1*b))/(2*a)
    imaginary_part = (math.sqrt((-1*d)))/(2*a)
    r1=complex(real_part, imaginary_part)
    imaginary_part*=-1
    r2=complex(real_part, imaginary_part)
print(r1)
print(r2)