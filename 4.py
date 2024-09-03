name = input("Enter the name")
roll = int(input("Enter the roll number"))
marks = int(input("Enter the marks"))
grade = 10
if(marks>=80 and marks<90) :
    grade=9
elif(marks>=70 and marks<80) :
    grade=8
elif(marks>=60 and marks<70) :
    grade=7
elif(marks>=50 and marks<60) :
    grade=6
else :
    grade=0
remark = 'OUTSTANDING'
if(grade==9):
    remark = 'VERY GOOD'
elif(grade==8):
    remark = 'GOOD'
elif(grade==7):
    remark = 'AVERAGE'
elif(grade==6):
    remark = 'PASS'
else :
    remark = 'FAIL'
dict={'NAME':name, 'ROLL NO':roll, 'MARKS':marks, 'GRADE':grade, 'REMARKS':remark}
print(dict)